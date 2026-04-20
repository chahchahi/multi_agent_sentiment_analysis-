from crewai import Agent
from src.tools.reddit_tool import RedditDataTool
from src.config import get_llm

class RedditDataAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Reddit Data Collector",
            goal="Collect relevant data from Reddit based on the given topic",
            backstory="You are an expert at gathering information from Reddit. You use tools to fetch posts from relevant subreddits.",
            tools=[RedditDataTool()],
            llm=get_llm(),
            verbose=True
        )