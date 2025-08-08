import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import joblib
import os

os.makedirs('model', exist_ok=True)

df = pd.read_csv('data/bns_sections_cleaned.csv')

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])

model = NearestNeighbors(n_neighbors=3, metric='cosine')
model.fit(X)

joblib.dump(model, 'model/model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')
print("✅ Model and vectorizer saved to model/")
