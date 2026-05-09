from crewai import Agent
from crewai_tools import SerperDevTool
from src.config import get_llm

class ResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Research Agent",
            goal=(
                "Search ONLY within the specified website for articles related to the user-provided topic. "
                "Use site-specific search queries to find content exclusively from that domain. "
                "Return article titles, URLs, snippets, and reference citations from that website only."
            ),
            backstory=(
                "You are a focused researcher who searches exclusively within a specified website/domain. "
                "You use targeted search queries to find relevant articles only from the given website, "
                "ignoring results from other sources."
            ),
            tools=[SerperDevTool()],
            llm=get_llm(),
            verbose=True
        )
