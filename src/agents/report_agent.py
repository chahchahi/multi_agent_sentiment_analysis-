from crewai import Agent
from src.config import get_llm

class ReportAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Report Writer Agent",
            goal="Write a clear markdown report summarizing each found article and including the original reference links.",
            backstory="You are a report writer who turns research results into plain-language markdown summaries with article references.",
            llm=get_llm(),
            verbose=True
        )
