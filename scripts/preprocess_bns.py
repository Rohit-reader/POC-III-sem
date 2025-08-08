import pandas as pd
import re

df = pd.read_csv("data/bns_sections_final.csv")

def clean_text(text):
    text = str(text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text.strip()

df['section_title'] = df['section_title'].apply(clean_text)
df['content'] = df['content'].apply(clean_text)

df.to_csv("data/cleaned_bns.csv", index=False)
print("✅ Cleaned data saved as cleaned_bns.csv")
