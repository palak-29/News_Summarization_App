# 📰 AI-Powered News Summarizer + Sentiment Analyzer + Hindi TTS 🎙️

![banner](https://img.shields.io/badge/Powered_by-Streamlit-FF4B4B?logo=streamlit) ![hugging-face](https://img.shields.io/badge/Hugging%20Face-Deployed-yellow?logo=huggingface) ![license](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 🚀 Overview

A complete AI solution to:
- 📥 Scrape live news articles about any company
- 📝 Summarize each article using BART
- 🧠 Run sentiment analysis (Positive / Negative / Neutral)
- 🔍 Extract key topics using NLP (KeyBERT)
- 📊 Generate comparative sentiment analysis with interactive charts
- 🎙️ Convert insights into **Hindi audio** using Google TTS (gTTS)
- 🌐 Deployable via Hugging Face Spaces (Streamlit App)

---

## 🛠️ Tech Stack

- **Streamlit** for the web UI
- **FastAPI** (optional) for backend APIs
- **BeautifulSoup** for RSS scraping
- **Hugging Face Transformers** for summarization & sentiment
- **KeyBERT** for keyword extraction
- **gTTS** for Hindi audio synthesis
- **Plotly** for pie chart visualization

---

## 📊 Features

- Extracts up to **25 news articles** via Google News RSS
- **Auto-summarizes articles** using `facebook/bart-large-cnn`
- **Sentiment analysis** with `cardiffnlp/twitter-roberta-base-sentiment` (or optional DistilBERT)
- **Keyword extraction** with KeyBERT
- Displays **interactive pie charts** of sentiment distribution
- Generates **Hindi audio insights** for accessibility

---

## 🖼️ Screenshots

| 📄 Articles with Sentiment | 📊 Sentiment Pie Chart | 🎧 Hindi TTS Audio |
|----------------------------|-----------------------|--------------------|
| ![articles](output/articles.png) | ![chart](output/piechart.png) | ![audio](output/audio.png) |

---

## 🚀 How to Run Locally

### Clone the repo:
```bash
git clone https://github.com/your-username/news-summarizer-hindi-tts.git
cd news-summarizer-hindi-tts

Install dependencies:
pip install -r requirements.txt
Run the app (Streamlit):
streamlit run app.py


news-summarization-app/
├── app.py                # Hugging Face-friendly Streamlit app
├── utils.py              # NLP & TTS helpers
├── requirements.txt
└── README.md             # You're here!

🧪 Example Flow:

Enter company name (e.g., "Tesla")
System scrapes news articles + generates:
Title
Summary
Sentiment
Topics
Pie chart & Hindi audio insight are generated automatically
🎧 Hindi Insight Example:

"Sampurn 25 samachaaron mein se 15 Positive, 7 Negative, aur 3 Neutral hain. Kul milaakar coverage Positive hai."

🟢 Live Demo

👉 Deployed on Hugging Face Spaces: Click here!

🤖 To-Do / Improvements

 Add PDF/CSV report export
 Deploy full API + frontend on Render or AWS
 Optional: Enable multilingual TTS (e.g., English & Hindi)

🙌 Credits

Hugging Face 🤗 for open-source models.
Streamlit Team for making deployment easy.
gTTS for free Hindi TTS.
