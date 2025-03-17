# utils.py

import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS
import os
from collections import Counter
import re

# Load models once globally
summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_model = pipeline('sentiment-analysis', model="cardiffnlp/twitter-roberta-base-sentiment")

# 1. Scrape News
def scrape_news(company):
    feed_url = f"https://news.google.com/rss/search?q={company}&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(feed_url)
    soup = BeautifulSoup(response.content, features="lxml-xml")
    articles = []
    items = soup.findAll('item')[:10]
    for item in items:
        title = item.title.text
        link = item.link.text
        pub_date = item.pubDate.text
        articles.append({'title': title, 'link': link, 'published': pub_date})
    return articles

# 2. Summarize text
def summarize_text(text):
    summary = summarizer_model(text, max_length=50, min_length=20, do_sample=False)
    return summary[0]['summary_text']

# 3. Sentiment Analysis
def analyze_sentiment(text):
    result = sentiment_model(text)
    label = result[0]['label']
    mapping = {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive"}
    return mapping.get(label, "Unknown")

# 4. Extract Topics (simple keyword extraction)
def extract_topics(text):
    words = re.findall(r'\b\w{4,}\b', text.lower())
    common_words = {'microsoft', 'launches', 'news', 'update'}
    keywords = [word for word in words if word not in common_words]
    top_keywords = Counter(keywords).most_common(3)
    return [kw[0].capitalize() for kw in top_keywords]

# 5. Generate Comparative Summary + Hindi TTS
def comparative_analysis(all_sentiments):
    counts = Counter(all_sentiments)
    pos = counts.get("Positive", 0)
    neg = counts.get("Negative", 0)
    neu = counts.get("Neutral", 0)
    total = pos + neg + neu
    overall = max(counts, key=counts.get) if counts else "Neutral"

    insight = f"Sampurn {total} samachaaron mein se {pos} Positive, {neg} Negative, aur {neu} Neutral hain. Kul milaakar coverage {overall} hai."
    
    # Generate Hindi TTS
    os.makedirs("static", exist_ok=True)
    tts = gTTS(insight, lang='hi')
    audio_path = "static/summary.mp3"
    tts.save(audio_path)

    return {
        "sentiment_distribution": dict(counts),
        "overall_sentiment": overall,
        "insight": insight,
        "audio_file": audio_path
    }
