import praw
from src.config import CLIENT_ID, SECRET_TOKEN, USER_AGENT, SP500

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = SECRET_TOKEN,
    user_agent = USER_AGENT
)

subredditWSB = reddit.subreddit('WallStreetBets')

sAndp = SP500

print(len(SP500))

# for submission in subredditWSB.new(limit =10):
#     print(submission.title)
#     print(submission.selftext)

#     print('----------------------------------------------')



##print(reddit.read_only)