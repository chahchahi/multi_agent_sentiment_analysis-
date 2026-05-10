from crewai import Task

from src.agents.report_agent import ReportAgent
from src.agents.auditor_agent import AuditorAgent
from src.agents.sentiment_agent import SentimentAgent
from src.agents.research_agent import WebsiteResearchAgent
from src.agents.research_agent import NewsResearchAgent




def create_research_tasks(website=None):
    """Create and return the research workflow tasks."""
    research_agent = WebsiteResearchAgent()
    auditor_agent = AuditorAgent()
    report_agent = ReportAgent()
    sentiment_agent = SentimentAgent()
    news_research_agent = NewsResearchAgent()
    if website: 
        print(f"Creating tasks for website-specific research on: {website}")
        search_task = Task(
            description=(
                "Search EXCLUSIVELY within the website {website} for articles related to '{topic}'. "
                "Use the 'Site Search Tool' with the query 'site:{website} {topic}'. "
                "Only return results from {website}. "
                "Make ONE search query only. Do not repeat or refine the search."
            ),
            agent=research_agent,
            expected_output=(
                "A list of articles references from {website} only, "
                "with title, url, snippet, and source name."
            )
        )
    else:
        print(f"Creating tasks for new research ")
        search_task = Task(
            description=(
                "Search Google News for articles related to '{topic}'. "
                "Use the 'News Search Tool' to find recent news articles. "
                "Make ONE search query only. Do not repeat or refine the search.\n"
                "\n"
                "STRICT RULES:\n"
                "- EXCLUDE results from: wikipedia.org, reddit.com, quora.com, "
                "  youtube.com, imdb.com, and any encyclopaedia or social media sites.\n"
                "- ONLY return results from recognised news outlets such as "
                "  bbc.com, irishtimes.com, rte.ie, theguardian.com, reuters.com.\n"
                "- If a result is not from a news outlet, discard it.\n"
            ),
            agent=news_research_agent,
            expected_output=(
                "A list of news article references with title, url, snippet, and source name. "
                "No Wikipedia, social media, or non-news results."
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
        context=[audit_task],
        async_execution=True
    )

    sentiment_task = Task(
    description=(
        "For each verified article provided in the context, analyse how the topic '{topic}' "
        "is specifically portrayed and discussed within the article. "
        "\n\n"
        "Your classification must answer this question:\n"
        "  'How does this article portray or frame {topic} specifically?'\n"
        "\n"
        "Follow these strict classification rules:\n"
        "- **Positive**: The article portrays {topic} favourably — sympathetically, "
        "  admiringly, supportively, or highlights their achievements and resilience.\n"
        "- **Negative**: The article portrays {topic} unfavourably — critically, "
        "  as a threat, or in a damaging light.\n"
        "- **Neutral**: The article mentions {topic} factually without clear positive "
        "  or negative framing toward them specifically.\n"
        "\n"
        "IMPORTANT RULES:\n"
        "- Focus ONLY on how {topic} is portrayed — not the general tone of the article.\n"
        "- An article can be alarming in tone but still portray {topic} positively "
        "  (e.g. a report about persecution of Bahá'ís is sympathetic TOWARD Bahá'ís "
        "  even though the topic of persecution is distressing).\n"
        "- Justify your classification with a direct reference to how {topic} "
        "  is described or framed in the article."
    ),
    agent=sentiment_agent,
    expected_output=(
        "For each article provide:\n"
        "- Title\n"
        "- Sentiment toward '{topic}': Positive / Negative / Neutral\n"
        "- Confidence: High / Medium / Low\n"
        "- Justification: One sentence explaining how '{topic}' is specifically "
        "  portrayed in this article."
    ),
    context=[audit_task],
    async_execution=True
   )

    final_task = Task(
        description=(
            "Combine the markdown report and the sentiment analysis results into one final report. "
            "For each article, display the summary followed immediately by its sentiment, "
            "confidence level, and justification. "
            "At the end of the report, include an overall analysis of the sentiment trends across all articles."
        ),
        agent=report_agent,
        expected_output=(
            "A single markdown document with each article's summary and sentiment analysis combined."
        ),
        context=[report_task, sentiment_task],
        async_execution=False
    )


     # ── Return both dictionaries ──────────────────────────────────────
    agents = {
        "research_agent": research_agent if website else news_research_agent,
        "auditor_agent": auditor_agent,
        "report_agent": report_agent,
        "sentiment_agent": sentiment_agent,
    }

    tasks = {
        "search_task": search_task,
        "audit_task": audit_task,
        "report_task": report_task,
        "sentiment_task": sentiment_task,
        "final_task": final_task,
    }

    return agents, tasks