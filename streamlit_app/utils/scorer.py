from .parser import scrape_url, extract_text_from_html
from .features import compute_features, predict_quality, find_similar
import pandas as pd
import os
from sentence_transformers import SentenceTransformer

# Load sentence transformer model once (efficient)
model = SentenceTransformer("all-MiniLM-L6-v2")

def analyze_url(url):
    # 1️⃣ Scrape and extract content
    html = scrape_url(url)
    title, text = extract_text_from_html(html)

    # 2️⃣ Compute basic linguistic features
    word_count, sentence_count, readability = compute_features(text)
    label = predict_quality(word_count, sentence_count, readability)
    is_thin = word_count < 500

    # 3️⃣ Load reference corpus
    data_path = os.path.join(os.path.dirname(__file__), "../../data/features.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}. Please upload features.csv to /data/.")
    
   corpus = pd.read_csv(os.path.join(os.path.dirname(__file__), "../../data/features.csv"))

# Try to find the correct text column dynamically
possible_cols = ["text", "content", "body_text", "clean_text", "article"]
text_col = next((c for c in possible_cols if c in corpus.columns), None)

if text_col is None:
    raise KeyError("No valid text column found in features.csv. Expected one of: text, content, body_text, clean_text, article")

# Encode corpus text using the correct column
corpus_embeddings = model.encode(corpus[text_col].astype(str).tolist())

    # 5️⃣ Find most similar pages
    top_urls, duplicate = find_similar(query_emb, corpus_embeddings, corpus_urls)

    # 6️⃣ Return structured result
    return {
        "url": url,
        "title": title,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "readability": readability,
        "quality_label": label,
        "is_thin": is_thin,
        "duplicate": duplicate,
        "similar_pages": top_urls,  # List of (url, score)
    }
