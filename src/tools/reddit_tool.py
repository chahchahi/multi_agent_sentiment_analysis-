import praw
from crewai_tools import BaseTool
import os

class RedditDataTool(BaseTool):
    name: str = "Reddit Data Fetcher"
    description: str = "Fetches recent posts from a specified subreddit"

    def _run(self, subreddit: str, limit: int = 10) -> str:
        reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT', 'sentiment_analysis_bot')
        )

        subreddit_obj = reddit.subreddit(subreddit)
        posts = []

        for post in subreddit_obj.hot(limit=limit):
            posts.append({
                'title': post.title,
                'selftext': post.selftext,
                'score': post.score,
                'url': post.url,
                'author': str(post.author),
                'created_utc': post.created_utc
            })

        return str(posts)