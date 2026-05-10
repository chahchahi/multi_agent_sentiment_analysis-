from crewai import Agent
from crewai_tools import SerperDevTool
from src.config import get_llm

from crewai import Agent
from crewai_tools import SerperDevTool
from src.config import get_llm


class WebsiteResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Research Agent",
            goal=(
                "Search for articles related to the user-provided topic. "
                "Search exclusively within that domain. of the website provided by the user. "
                "Return article titles, URLs, snippets, and reference citations."
            ),
            backstory=(
                "You are a versatile researcher skilled at finding relevant articles "
                "from both specific websites"
                "You adapt your search strategy based on whether a target website is provided. "
                "You always use precise, targeted queries to find the most relevant content "
                "and ignore results from unintended sources."
            ),
            tools=[
                SerperDevTool(n_results=10)                                   # ← general web search
            ],
            llm=get_llm(),
            verbose=True
        )

class NewsResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Research Agent",
            goal=(
                "Search for articles related to the user-provided topic. "
                "Search across reputable news sources on Google News. "
                "Focus more on recent news coverage and ensure results are from news outlets, not Wikipedia, social media, or other non-news sources. "
                "Return article titles, URLs, snippets, and reference citations."
            ),
            backstory=(
                "You are a versatile researcher skilled at finding relevant articles "
                "from both specific websites and broader news sources. "
                "You always use precise, targeted queries to find the most relevant content "
                "and ignore results from unintended sources."
            ),
            tools=[
                SerperDevTool(
                    n_results=10,
                    search_type="news",   # ← correct parameter (not search_url)
                    name="News Search Tool",
                    description="Searches Google News for recent news articles only."
                )
            ],
            llm=get_llm(),
            verbose=True
        )