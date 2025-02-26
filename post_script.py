import praw
import os

# Reddit API authentication
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Post details
subreddit_name = "UIUC"  # Change this
title = "Summer Sublease 4b2b Female Unit"
body = "Hi! I have a room in a 4b2b unit available from Jan-July. Rent is $750/month (negotiable), utilities vary but are usually less than $50/month. The address is 901 S Second St. Included are: in-unit washer/dryer, giant balcony, large TV, lots of storage space. 10 minute walk from the quad, and bus stop very close. Let me know!"
flair_text = "Sublease"  # The text of the tag (flair)

# Submit the post
subreddit = reddit.subreddit(subreddit_name)
submission = subreddit.submit(title, selftext=body)
submission.flair.select("Sublease")  # Replace with actual flair ID
