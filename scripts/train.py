import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Load and clean dataset
df = pd.read_csv('data/fir_dataset.csv')
df.dropna(inplace=True)  # 🔥 Remove rows with empty values

X = df['incident']
y = df['law_sections']
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X, y)
os.makedirs('model', exist_ok=True)
joblib.dump(pipeline, 'model/fir_model.pkl')
print("✅ Model trained and saved.")
