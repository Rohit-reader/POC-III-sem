import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/cleaned_bns.csv")
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['content'])

def recommend(query, top_n=3):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    if max(similarities) < 0.05:
        return None

    indices = similarities.argsort()[-top_n:][::-1]
    return df.iloc[indices][['section_number', 'section_title', 'content']]
