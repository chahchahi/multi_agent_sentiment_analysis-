from crewai import Agent
from src.tools.sentiment_tool import SentimentAnalysisTool
from src.config import get_llm

class SentimentAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Sentiment Classifier",
            goal="Classify the sentiment of each message as positive, negative, or neutral",
            backstory="You are an expert in analyzing emotions and opinions in text. You use specialized tools to determine the sentiment of messages accurately.",
            tools=[SentimentAnalysisTool()],
            llm=get_llm(),
            verbose=True
        )