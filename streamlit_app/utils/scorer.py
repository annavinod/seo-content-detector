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
    
    corpus = pd.read_csv(data_path)

    # 4️⃣ Create embeddings for new page + corpus
    query_emb = model.encode(text)
    corpus_embeddings = model.encode(corpus["text"].astype(str).tolist())
    corpus_urls = corpus["url"].tolist()

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
