from crewai import Crew, Task
from src.agents.reddit_agent import RedditDataAgent
from src.agents.summarizer_agent import SummarizerAgent
from src.agents.sentiment_agent import SentimentAgent
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Initialize agents
    reddit_agent = RedditDataAgent()
    summarizer_agent = SummarizerAgent()
    sentiment_agent = SentimentAgent()

    # Define tasks
    collect_data_task = Task(
        description="Collect recent posts from Reddit related to the topic: {topic}",
        agent=reddit_agent,
        expected_output="A list of Reddit posts related to the topic"
    )

    summarize_task = Task(
        description="Summarize the key points and discussions from the collected Reddit data",
        agent=summarizer_agent,
        expected_output="A concise summary of the topic-related content",
        context=[collect_data_task]
    )

    sentiment_task = Task(
        description="Analyze the sentiment of each message in the collected data and classify as positive, negative, or neutral",
        agent=sentiment_agent,
        expected_output="Sentiment analysis for each message: positive, negative, or neutral",
        context=[collect_data_task]
    )

    # Create crew
    crew = Crew(
        agents=[reddit_agent, summarizer_agent, sentiment_agent],
        tasks=[collect_data_task, summarize_task, sentiment_task],
        verbose=True
    )

    # Run the crew
    result = crew.kickoff(inputs={"topic": "artificial intelligence"})
    print(result)

if __name__ == "__main__":
    main()