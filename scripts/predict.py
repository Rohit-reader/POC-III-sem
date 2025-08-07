import joblib

model = joblib.load('model/fir_model.pkl')

def predict_laws(text):
    return model.predict([text])[0]
