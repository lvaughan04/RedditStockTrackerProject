This is a text file to help me plan out my application



1. Configure the scraper and figure out how to get my data into the database
    a. How should the data be organized
        i. Timestamp
        ii. Subreddit
        iii. Link
        iv. Title
        v. Content

So First I get all of the posts within the last hour:

If a post has a stock mentioned say Google, it will search the sp500 dict and find that stock. If the stock mentioned is in sp500,
    then i want to save that post to the database, under the google collection
    what will be displayed will be a bar graph of all stocks mentioned by getting the number of posts in each stock collection

    the posts will be made up of 
        i. Timestamp
        ii. Subreddit
        iii. URL
        iv. Title
        v. Content

Way to make sure no duplicates
Check the title of the latest post in the database, store that in a variable, then go through the subreddit.new until that post is found or an hour has passed


So I need to get all 503 stocks into my database with what industry they are in as well for further filters to see the data clearly
