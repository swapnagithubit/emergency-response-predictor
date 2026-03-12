import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

df = pd.read_csv("../data/911_calls.csv")

df = df.dropna()

X = df["title"]
y = df["reason"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(X, y)

joblib.dump(model, "../models/emergency_classifier.pkl")

print("Model trained successfully")
