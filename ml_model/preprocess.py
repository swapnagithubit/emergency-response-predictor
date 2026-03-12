import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess(df):

    df = df.dropna()

    X = df['title']
    y = df['reason']

    encoder = LabelEncoder()
    y = encoder.fit_transform(y)

    return train_test_split(X, y, test_size=0.2)
