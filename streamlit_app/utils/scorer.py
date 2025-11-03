from .parser import scrape_url, extract_text_from_html
from .features import compute_features, predict_quality, find_similar
import pandas as pd
import os

def analyze_url(url):
    html = scrape_url(url)
    title, text = extract_text_from_html(html)
    word_count, sentence_count, readability = compute_features(text)
    label = predict_quality(word_count, sentence_count, readability)
    is_thin = word_count < 500

    corpus = pd.read_csv(os.path.join(os.path.dirname(__file__), "../../data/features.csv"))
    similar_urls = find_similar(text, corpus, corpus["url"].tolist())

    return {
        "url": url,
        "title": title,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "readability": readability,
        "quality_label": label,
        "is_thin": is_thin,
        "similar_to": similar_urls[:5],
    }
