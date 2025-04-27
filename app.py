import praw
import os
import pandas as pd
from textblob import TextBlob

from dotenv import load_dotenv

# Load API keys
load_dotenv()
API_KEY = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

# reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
#                      client_secret=os.getenv("REDDIT_SECRET"),
#                      user_agent="sentiment-analysis")



# Fetch top posts from a subreddit
subreddit_name = "technology"  # Change to your desired subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.hot(limit=100)
