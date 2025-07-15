# File: modules/sentiment.py

import feedparser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_news_sentiment(symbol, count=5):
    """
    Fetch the top `count` headlines from Yahoo Finance RSS
    and return the average VADER sentiment score.
    """
    feed_url = f"https://finance.yahoo.com/rss/2.0/headline?s={symbol}&lang=en-US"
    data = feedparser.parse(feed_url)
    titles = [entry.title for entry in data.entries[:count]]
    scores = [analyzer.polarity_scores(title)['compound'] for title in titles]
    return sum(scores) / len(scores) if scores else 0.0
