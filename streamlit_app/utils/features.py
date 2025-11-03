import textstat
import numpy as np
from nltk.tokenize import sent_tokenize
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

def find_similar(text, corpus, corpus_urls, threshold=0.75):
    if embedder is None:
        return []
    new_emb = embedder.encode([text])
    corpus_emb = np.load(os.path.join(os.path.dirname(__file__), "../../data/embeddings.npy"))
    sims = cosine_similarity(new_emb, corpus_emb).flatten()
    indices = np.where(sims > threshold)[0]
    return [{"url": corpus_urls[i], "similarity": float(sims[i])} for i in indices]
