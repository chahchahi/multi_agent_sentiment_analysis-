# Multi-Agent Website Article Research

A Python project using CrewAI to implement a multi-agent system for researching articles on specific websites. The system consists of three specialized agents:

1. **Research Agent**: Searches for articles on a specified website related to user-provided topics
2. **Auditor Agent**: Verifies and validates the found articles for relevance and accuracy
3. **Report Agent**: Creates comprehensive markdown reports summarizing the verified articles

## Features

- Targeted website article search using Google search with site-specific queries
- Intelligent article verification and relevance checking
- Automated report generation with article summaries and references
- Modular agent-based architecture using CrewAI

## Prerequisites

- Python 3.12+
- Serper API key for Google search functionality

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
   - Copy `.env` file and add the following API keys:
     - `SERPER_API_KEY=<your_serper_api_key>` for Google search support via Serper
   - Get Serper API key from [Serper.dev](https://serper.dev/)
   - Install Ollama from [ollama.ai](https://ollama.ai/) and pull a model (e.g., `ollama pull llama3.2`)
   - Optionally set `OLLAMA_MODEL=<model_name>` and `OLLAMA_BASE_URL=<url>` in `.env` (defaults to mistral and http://localhost:11434)

## Usage

Run the main script with topic and website parameters:

```bash
python -m src.main "topic name" "https://example.com"
```


The system will search for articles on the specified website related to your topic and generate a comprehensive report.

## Project Structure

```
src/
├── agents/
│   ├── research_agent.py    # Website search and article discovery agent
│   ├── auditor_agent.py     # Article verification and validation agent
│   └── report_agent.py      # Report generation and summarization agent
├── tools/
│   ├── reddit_tool.py       # Reddit API integration tool (legacy)
│   └── sentiment_tool.py    # Sentiment analysis tool (legacy)
├── config.py                # Configuration management
├── main.py                  # Main crew execution script
└── testing.py               # Testing utilities
```

## Dependencies

- crewai: Multi-agent framework
- crewai-tools: Collection of tools including SerperDevTool for web search
- python-dotenv: Environment variable management
- Other dependencies as specified in requirements.txt

## License

See LICENSE file for details.

