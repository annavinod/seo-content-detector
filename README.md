# SEO Content Quality & Duplicate Detector

## Overview
A complete NLP pipeline to evaluate webpage SEO quality and detect duplicates.

## How to Run
1. Clone the repository:
   git clone https://github.com/yourusername/seo-content-detector
   cd seo-content-detector

2. Install dependencies:
   pip install -r requirements.txt

3. Launch the notebook:
   jupyter notebook notebooks/seo_pipeline.ipynb

## Outputs
- data/extracted_content.csv
- data/features.csv
- data/duplicates.csv
- models/quality_model.pkl

## Key Results
- Duplicate threshold: 0.8
- Thin content threshold: 500 words
- Classifier: RandomForest
