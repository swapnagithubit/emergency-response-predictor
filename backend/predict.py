import joblib

model = joblib.load("../models/emergency_classifier.pkl")

def predict_emergency(text):

    prediction = model.predict([text])[0]

    return prediction
