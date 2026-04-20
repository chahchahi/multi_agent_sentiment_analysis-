from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """Initialize and return Ollama LLM instance"""
    return Ollama(
        model=os.getenv('OLLAMA_MODEL', 'mistral'),
        base_url=os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
    )
