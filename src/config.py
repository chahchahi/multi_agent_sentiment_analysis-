from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """Initialize and return OpenAI Open 4.1 Mini LLM instance"""
    return LLM(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),  # Or set OPENAI_API_KEY
    temperature=0.7,
    max_tokens=4000
)
