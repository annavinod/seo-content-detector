🚀 SEO Content Quality & Duplicate Detector
🧠 Overview

A machine learning and NLP pipeline that evaluates webpage SEO quality, readability, and detects duplicate or thin content.
It parses HTML, extracts key linguistic and structural features, computes similarity between pages, and predicts overall content quality (Low / Medium / High).

⚙️ Setup Instructions
git clone https://github.com/annavinod/seo-content-detector
cd seo-content-detector
pip install -r requirements.txt
jupyter notebook notebooks/seo_pipeline.ipynb

⚡ Quick Start

1️⃣ Open the notebook notebooks/seo_pipeline.ipynb
2️⃣ Run all cells to reproduce the entire pipeline
3️⃣ For real-time analysis, use:

result = analyze_url("https://example.com/article")
print(result)

🌐 Deployed Streamlit App

👉 Click here to view the live app

🔍 Key Features

HTML Parsing: Extracts clean body text and metadata using BeautifulSoup

Feature Engineering: Word count, sentence count, Flesch Reading Ease, top keywords, embeddings

Duplicate Detection: Cosine similarity on TF-IDF or embeddings to flag near-duplicates

Quality Scoring: Classifies each page as Low, Medium, or High using Random Forest

Real-Time Demo: Live URL analysis directly in the Streamlit app

📊 Results Summary

Model: Random Forest Classifier

Accuracy: 0.78

F1-Score: 0.77

Duplicate Pairs: 3

Thin Content Pages: 6 (≈10%)

💡 Key Decisions

Libraries: Used beautifulsoup4, textstat, sentence-transformers, and scikit-learn for efficiency and reliability.

Threshold: Set similarity cutoff at 0.80 for near-duplicate detection.

Model: Random Forest chosen for interpretability and consistent performance.

HTML Parsing Strategy: Focused on <p>, <article>, and <main> tags for meaningful content extraction.

⚠️ Limitations

Complex or script-heavy pages may have incomplete text extraction.

Readability metrics depend on textual density and type.

Quality labels were synthetically generated — human-labeled SEO data would improve accuracy.

✅ Evaluation Checklist

 End-to-end pipeline runs in Jupyter

 Real-time analyze_url() function works

 Streamlit app deployed successfully

 Clean project structure with documentation

 GitHub repo public and reproducible
