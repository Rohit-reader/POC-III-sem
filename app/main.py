from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__, static_folder='static', template_folder='templates')

df = pd.read_csv('data/bns_sections_cleaned.csv')
model = joblib.load('model/model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    incident = data.get('incident', '')

    if not incident:
        return jsonify({'error': 'No incident description provided'}), 400

    vec = vectorizer.transform([incident])
    distances, indices = model.kneighbors(vec)

    results = []
    for i in indices[0]:
        results.append({
            'section_number': df.iloc[i]['section_number'],
            'section_title': df.iloc[i]['section_title'],
            'content': df.iloc[i]['content']
        })

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
