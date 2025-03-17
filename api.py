# -*- coding: utf-8 -*-
# api.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import scrape_news, summarize_text, analyze_sentiment, extract_topics, comparative_analysis

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_news_report")
def get_news_report(company: str = Query(...)):
    raw_articles = scrape_news(company)
    final_articles = []
    sentiment_list = []

    for article in raw_articles:
        title = article['title']
        summary = summarize_text(title)
        sentiment = analyze_sentiment(title)
        topics = extract_topics(title + " " + summary)

        sentiment_list.append(sentiment)
        final_articles.append({
            "title": title,
            "summary": summary,
            "sentiment": sentiment,
            "topics": topics,
            "link": article['link'],
            "published": article['published']
        })

    comparison = comparative_analysis(sentiment_list)

    return {
        "company": company,
        "articles": final_articles,
        "comparative_analysis": {
            "sentiment_distribution": comparison["sentiment_distribution"],
            "overall_sentiment": comparison["overall_sentiment"],
            "insight": comparison["insight"]
        },
        "hindi_tts_audio": comparison["audio_file"]
    }
