# 🚀 SEO Content Quality & Duplicate Detector  

### 📘 Project Overview
This project delivers an **end-to-end AI + NLP pipeline** to evaluate webpage SEO content quality and detect near-duplicates.  
It intelligently parses HTML, extracts linguistic and structural features, computes content similarity,  
and predicts overall quality — **Low**, **Medium**, or **High** — using machine learning.  

---

## ⚙️ Tech Stack
**Languages:** Python 3.9+  
**Core Libraries:** `BeautifulSoup4`, `textstat`, `sentence-transformers`, `scikit-learn`, `pandas`, `nltk`  
**Interface:** Jupyter Notebook & Streamlit (for real-time analysis)  

---

## 🧩 Features
✅ **HTML Parsing:** Extracts titles and main body text from raw HTML  
✅ **Feature Engineering:** Word/sentence count, readability (Flesch), TF-IDF keywords, embeddings  
✅ **Duplicate Detection:** Cosine similarity on embeddings or TF-IDF vectors  
✅ **Thin Content Flagging:** Identifies low-word-count pages (<500 words)  
✅ **Quality Scoring Model:** Random Forest classifier for SEO quality prediction  
✅ **Real-Time Demo:** Live Streamlit app for instant URL evaluation  

---

## 🧠 Workflow
Input HTML/URLs → Clean & Parse → Extract NLP Features → Detect Duplicates →
Train Quality Model → Predict (Low / Medium / High) → Real-Time Streamlit Analysis

yaml
Copy code

---

## ⚙️ Setup Instructions
```bash
# Clone the repository
git clone https://github.com/annavinod/seo-content-detector
cd seo-content-detector

# Install dependencies
pip install -r requirements.txt

# Launch the main notebook
jupyter notebook notebooks/seo_pipeline.ipynb
⚡ Quick Start
python
Copy code
from utils.scorer import analyze_url

# Analyze any webpage URL in real-time
result = analyze_url("https://example.com/article")
print(result)
🌐 Live Demo
🎯 Try it here: SEO Content Detector App →

Analyze any live webpage for readability, SEO score, and duplication — directly from your browser.

📊 Model Performance
Metric	Score
Model	Random Forest Classifier
Accuracy	0.78
F1-Score	0.77
Duplicate Pairs	3
Thin Content Pages	6 (≈10%)

💡 Key Design Decisions
Parsing Strategy: Focused on <p>, <article>, and <main> for core content extraction

Similarity Threshold: Cosine similarity ≥ 0.80 → duplicate

Feature Selection: Chose readability + count features + embeddings for explainability

Model Choice: Random Forest for stability and interpretability over deep models

⚠️ Limitations
Pages heavy with JavaScript or structured markup may yield incomplete text extraction

Readability metrics can vary by domain type (technical vs. general audience)

Current quality labels are synthetic — human-labeled SEO data would improve performance

✅ Evaluation Checklist
 End-to-end pipeline executes without errors

 Real-time analyze_url() function operational

 Streamlit app deployed & stable

 Clean modular codebase

 Well-documented and reproducible project

🏁 Submission Summary
Status: ✔️ Complete & Deployed
Bonus: Streamlit Cloud Deployment Achieved
Author: Anna Vinod
Live Demo: seo-content-detector-9wgjet3hafdemayusgyn9j.streamlit.app

“Data is the new SEO — structured, measurable, and intelligent.” 🌐✨
