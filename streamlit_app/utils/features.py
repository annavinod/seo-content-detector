import textstat
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt_tab')
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "../models/quality_model.pkl")
quality_model = joblib.load(model_path)

try:
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:
    embedder = None

def compute_features(text):
    sentences = sent_tokenize(text)
    sentence_count = len(sentences)
    readability = textstat.flesch_reading_ease(text)
    word_count = len(text.split())
    return word_count, sentence_count, readability

def predict_quality(word_count, sentence_count, readability):
    features = np.array([[word_count, sentence_count, readability]])
    return quality_model.predict(features)[0]

def find_similar(query_embedding, corpus_embeddings, corpus_urls, threshold=0.8):
    # Ensure both embeddings are proper numpy arrays with 2D shape
    query_embedding = np.array(query_embedding).reshape(1, -1)
    corpus_embeddings = np.array(corpus_embeddings)

    # Compute cosine similarity
    sims = cosine_similarity(query_embedding, corpus_embeddings)[0]

    # Sort results by similarity descending
    ranked = sorted(list(zip(corpus_urls, sims)), key=lambda x: x[1], reverse=True)
    top_matches = [(url, round(score * 100, 2)) for url, score in ranked[:3]]

    # Determine if any duplicates exceed threshold
    duplicate = any(score >= threshold for _, score in ranked)

    return top_matches, duplicate
