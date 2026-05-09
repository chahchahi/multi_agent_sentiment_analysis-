from crewai import Agent
from src.config import get_llm

class AuditorAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Auditor Agent",
            goal="Verify that collected articles are truly related to the topic and that the references are sensible and not hallucinated.",
            backstory="You are a careful auditor who validates article relevance, checks citations, and flags inconsistencies or irrelevant content.",
            llm=get_llm(),
            verbose=True
        )
