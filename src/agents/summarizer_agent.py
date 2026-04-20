from crewai import Agent
from src.config import get_llm

class SummarizerAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Content Summarizer",
            goal="Summarize topic-related content from collected data",
            backstory="You are skilled at condensing information and extracting key points from various sources. You create concise summaries that capture the essence of discussions.",
            llm=get_llm(),
            verbose=True
        )