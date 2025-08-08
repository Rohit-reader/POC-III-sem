from flask import Flask, request, render_template, jsonify
from model.predict import predict_section

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['user_input']
    results = predict_section(text)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
