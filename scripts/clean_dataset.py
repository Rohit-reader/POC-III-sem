import pandas as pd
import os

os.makedirs('data', exist_ok=True)

df = pd.read_csv('data/bns_sections_raw.csv')
df = df.dropna(subset=['section_number', 'content'])

df['section_number'] = df['section_number'].astype(str).str.strip()
df['section_title'] = df['section_title'].fillna('').astype(str).str.strip()
df['content'] = df['content'].astype(str).str.strip()
df['text'] = df['section_title'] + ". " + df['content']

df[['section_number', 'section_title', 'text']].to_csv('data/bns_sections_cleaned.csv', index=False)
print("✅ Cleaned data saved to data/bns_sections_cleaned.csv")
