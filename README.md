# Multi-Agent Sentiment Analysis

A Python project using CrewAI to implement a multi-agent system for sentiment analysis. The system consists of three specialized agents:

1. **Reddit Data Collector**: Fetches relevant posts from Reddit based on specified topics
2. **Content Summarizer**: Analyzes and summarizes topic-related discussions
3. **Sentiment Classifier**: Classifies the sentiment of each message as positive, negative, or neutral

## Features

- Automated data collection from Reddit
- Intelligent content summarization
- Sentiment analysis using natural language processing
- Modular agent-based architecture using CrewAI

## Prerequisites

- Python 3.8+
- Reddit API credentials (client ID and secret)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd multi-agent-sentiment-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Set up environment variables:
   - Copy `.env` file and fill in your Reddit API credentials
   - Get credentials from [Reddit Apps](https://www.reddit.com/prefs/apps)

## Usage

Run the main script:

```bash
python -m src.main
```

Or use the installed script:

```bash
run
```

The system will collect data on a default topic (artificial intelligence). Modify the `inputs` in `main.py` to change the topic.

## Project Structure

```
src/
├── agents/
│   ├── reddit_agent.py      # Reddit data collection agent
│   ├── summarizer_agent.py  # Content summarization agent
│   └── sentiment_agent.py   # Sentiment analysis agent
├── tools/
│   ├── reddit_tool.py       # Reddit API integration tool
│   └── sentiment_tool.py    # Sentiment analysis tool
└── main.py                  # Main crew execution script
```

## Dependencies

- crewai: Multi-agent framework
- praw: Reddit API wrapper
- textblob: Sentiment analysis library
- python-dotenv: Environment variable management

## License

See LICENSE file for details.
