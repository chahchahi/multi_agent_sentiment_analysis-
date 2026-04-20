# AI Coding Assistant Instructions for Multi-Agent Sentiment Analysis

## Project Overview
This is a CrewAI-based multi-agent system for sentiment analysis that collects Reddit data, summarizes content, and classifies sentiment. The system uses three specialized agents working in sequence.

## Architecture
- **Multi-Agent Framework**: Uses CrewAI for orchestrating agent interactions
- **Data Flow**: Reddit Collection → Content Summarization → Sentiment Classification
- **Tool-Based Agents**: Each agent uses custom tools for specific tasks

## Agent Patterns
- Agents inherit from `crewai.Agent` with role, goal, backstory, and tools
- Example: `RedditDataAgent` collects data using `RedditDataTool`
- All agents set `verbose=True` for debugging

## Tool Implementation
- Tools extend `crewai_tools.BaseTool` with `name`, `description`, and `_run` method
- Example: `SentimentAnalysisTool` uses TextBlob for polarity analysis
- Tools handle external APIs (Reddit via praw) and processing (sentiment via textblob)

## Code Structure
- `src/agents/`: Agent classes
- `src/tools/`: Custom tool implementations  
- `src/main.py`: Crew definition and execution
- Use `python -m src.main` to run (not `python src/main.py`)

## Dependencies & Environment
- Virtual environment required: `python -m venv .venv && source .venv/bin/activate`
- Install from `requirements.txt`: `pip install -r requirements.txt`
- Environment variables in `.env`: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
- Key packages: crewai, praw, textblob, pandas, matplotlib, seaborn

## Development Workflow
1. Activate venv: `source .venv/bin/activate`
2. Set Reddit API credentials in `.env`
3. Run: `python -m src.main`
4. Modify `inputs` in `main.py` to change topics

## Specific Conventions
- Agent backstories emphasize expertise and tool usage
- Tasks use `expected_output` for clear deliverables
- Context passing between tasks via `context=[previous_task]`
- Sentiment classification: polarity >0.1 positive, < -0.1 negative, else neutral
- Reddit data fetched as list of dicts with title, selftext, score, etc.

## Common Patterns
- Import agents/tools from `src.agents` / `src.tools`
- Use `load_dotenv()` in main scripts
- Crew tasks defined with description, agent, expected_output, and optional context
- Output typically string representations of data structures

## Testing & Validation
- Agents/tools can be tested individually before crew execution
- Check tool `_run` methods with sample inputs
- Validate sentiment polarity thresholds for accuracy

## Extension Points
- Add new tools in `src/tools/` extending BaseTool
- Create new agents in `src/agents/` following the pattern
- Modify task chain in `main.py` for different workflows
- Integrate additional data sources by creating new collection tools