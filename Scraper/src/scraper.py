import praw, pymongo
from datetime import datetime, timedelta
from config import CLIENT_ID, SECRET_TOKEN, USER_AGENT, SP500, COMMON_WORD_TICKERS, REDDIT_URL
from database import SP_COLLECTION, POSTS_COLLECTION

def create_post(submission):
    stock_symbols, url = check_for_stock(submission)
    if not stock_symbols:
        return False

    stock_ids = []

    for symbol in stock_symbols:
        stock = SP_COLLECTION.find_one({"Symbol": symbol})
        if stock:
            stock_ids.append(stock["_id"])

    post_document = {
        "url": url,
        "timestamp": datetime.now(),
        "subreddit": submission.subreddit.display_name,
        "author": submission.author.name if submission.author else "[deleted]",
        "title": submission.title,
        "body": submission.selftext,
        "stock_references": stock_ids
    }

    try: 
        POSTS_COLLECTION.insert_one(post_document)
        print("Post entered succesfully from " + submission.subreddit.display_name)
        return True
    except pymongo.errors.DuplicateKeyError:
        print("Duplicate key error: The post already exists in the database.")
    except Exception as e:
        print("Unexpected error occured when entering post", e)

## Returns an array of stocks mentioned. 
# Checks if a word appears in the stock list. If found then stock ticker is appended the result array.
def check_for_stock(submission):
    result = set()
    full_submission = submission.title + " " + submission.selftext
    for word in full_submission.split():
        word = word.upper()
        word = word.strip(".,!?()[]{}")

        if word in COMMON_WORD_TICKERS and not word.startswith("$"):
            continue
        
        if word.startswith("$"):
            word = word.lstrip("$")
        if word in SP500:
              result.add(word)
    link = REDDIT_URL + submission.permalink
    return result , link

def process_subreddit(subreddit, time_ago, posts_collection):
    last_post_ID = None
    
    for i, submission in enumerate(subreddit.new(limit=100, params={'after': last_post_ID})):
        submission_time = datetime.fromtimestamp(submission.created_utc)

        if submission_time <= time_ago:
            print("Submission was posted after time_threshold")
            return

        # Check if the post already exists in the database, we can exit the function since it will reach the last inserted post and will
        # have already checked the posts after it
        if posts_collection.find_one({"url": submission.url}):
            print("Already exists")
            return
            
        # Create a new post object and insert it into the database
        create_post(submission)

        if i == 99:
            last_post_ID = submission.id

def main():
    print("entered main method")

    REDDIT = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = SECRET_TOKEN,
        user_agent = USER_AGENT
    )

    subreddit_wsb = REDDIT.subreddit('wallstreetbets')
    subreddit_investing = REDDIT.subreddit('investing')
    subreddit_stocks = REDDIT.subreddit('stocks')
    subreddit_trading = REDDIT.subreddit('trading')
    subreddit_stock_market = REDDIT.subreddit('StockMarket')
    subreddit_options = REDDIT.subreddit('options')
    subreddit_value_investing = REDDIT.subreddit('ValueInvesting')

    day_ago = datetime.now() - timedelta(days=1)

    process_subreddit(subreddit_wsb, day_ago, POSTS_COLLECTION)
    process_subreddit(subreddit_investing, day_ago, POSTS_COLLECTION)
    process_subreddit(subreddit_stocks, day_ago, POSTS_COLLECTION)
    process_subreddit(subreddit_trading, day_ago, POSTS_COLLECTION)
    process_subreddit(subreddit_stock_market, day_ago, POSTS_COLLECTION)
    process_subreddit(subreddit_options, day_ago, POSTS_COLLECTION)
    process_subreddit(subreddit_value_investing, day_ago, POSTS_COLLECTION)


if __name__ == "__main__":
    main()