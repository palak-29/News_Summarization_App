# -*- coding: utf-8 -*-
# app.py

import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="News Analyzer + TTS", layout="wide")
st.title("📰 News Summarizer + Sentiment + Hindi TTS")
company = st.text_input("Enter Company Name:")

if st.button("Fetch Full Report"):
    if company:
        with st.spinner("Processing..."):
            response = requests.get(f"http://127.0.0.1:8000/get_news_report?company={company}")
            if response.status_code == 200:
                data = response.json()
                articles = data["articles"]
                comp = data["comparative_analysis"]

                for idx, article in enumerate(articles, 1):
                    st.subheader(f"🗞️ Article {idx}: {article['title']}")
                    st.caption(f"Published: {article['published']}")
                    st.markdown(f"[Read full article]({article['link']})")
                    st.write(f"**Summary:** {article['summary']}")
                    sentiment = article['sentiment']
                    if sentiment == "Positive":
                        st.success(f"Sentiment: {sentiment}")
                    elif sentiment == "Negative":
                        st.error(f"Sentiment: {sentiment}")
                    else:
                        st.info(f"Sentiment: {sentiment}")
                    st.write(f"**Topics:** {', '.join(article['topics'])}")

                # Pie Chart
                dist = comp["sentiment_distribution"]
                fig = go.Figure(data=[go.Pie(
                    labels=list(dist.keys()),
                    values=list(dist.values()),
                    hole=0.4,
                    marker=dict(colors=['green', 'red', 'skyblue']),
                    textinfo='value+percent'
                )])
                st.plotly_chart(fig, use_container_width=True)

                st.info(f"📝 Comparative Insight: {comp['insight']}")
                st.audio(data["hindi_tts_audio"])
            else:
                st.error("API Error.")
    else:
        st.warning("Please enter a company name.")
