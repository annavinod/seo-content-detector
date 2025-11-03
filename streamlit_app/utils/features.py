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


def find_similar(query_embedding, corpus_embeddings, corpus_urls, threshold=0.7):
    """Return top similar URLs with their similarity scores"""
    sims = cosine_similarity([query_embedding], corpus_embeddings)[0]
    top_idx = np.argsort(sims)[::-1][:3]  # top 3 matches
    top_urls = [(corpus_urls[i], float(sims[i])) for i in top_idx if sims[i] > threshold]
    duplicate = any(s > 0.85 for s in sims)  # less strict match
    return top_urls, duplicate
