import praw
import os
import pandas as pd
from textblob import TextBlob

from dotenv import load_dotenv

# Load API keys
load_dotenv()
API_KEY = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

# Using the config file
import config
api_key = config.API_KEY
api_secret = config.API_SECRET

reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_SECRET"),
                     user_agent="sentiment-analysis",
                     username = config.username,
                     password = config.password)



# Fetch top posts from a subreddit
subreddit_name = "technology"  # Change to your desired subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.hot(limit=100)
