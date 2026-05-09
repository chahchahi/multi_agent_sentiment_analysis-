from crewai import Task
from src.agents.research_agent import ResearchAgent
from src.agents.auditor_agent import AuditorAgent
from src.agents.report_agent import ReportAgent


def create_research_tasks(research_agent, auditor_agent, report_agent):
    """Create and return the research workflow tasks."""
    
    search_task = Task(
        description=(
            "Search EXCLUSIVELY within the website {website} for articles related to the topic '{topic}'. "
            "Use the 'Search the internet with Serper' tool with site-specific search queries like 'site:domain.com topic'. "
            "Only return articles that are actually from the specified website {website}. "
            "Return article titles, URLs, short snippets, and reference citations from {website} only. "
            "Format the query as: site:{website} {topic}. "
            "When there are multiple topics break down the topics , and format the query as: site:{website} (topic1 OR topic2 OR ...). "
            "Merge results and return only articles from {website}."
        ),
        agent=research_agent,
        expected_output=(
            "A list of article references from {website} only, with title, url, snippet, and reference information."
        )
    )

    audit_task = Task(
        description=(
            "Review the collected article references and verify each one is truly related to the topic {topic}. "
            "Confirm that the reference URLs make sense and flag any hallucinated or irrelevant items."
        ),
        agent=auditor_agent,
        expected_output=(
            "A cleaned list of articles that are topic-relevant and verifiably referenced, with auditor notes."
        ),
        context=[search_task]
    )

    report_task = Task(
        description=(
            "Write a plain-language markdown report summarizing each verified article found. "
            "Include the original reference link and a short summary for every article."
        ),
        agent=report_agent,
        expected_output=(
            "A markdown document with headings, article summaries, and original article references."
        ),
        context=[audit_task]
    )

    return search_task, audit_task, report_task
