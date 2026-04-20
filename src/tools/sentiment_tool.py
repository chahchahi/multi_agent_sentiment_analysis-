from textblob import TextBlob
from crewai_tools import BaseTool

class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analyzer"
    description: str = "Analyzes the sentiment of given text as positive, negative, or neutral"

    def _run(self, text: str) -> str:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return f"Sentiment: {sentiment} (polarity: {polarity:.2f})"