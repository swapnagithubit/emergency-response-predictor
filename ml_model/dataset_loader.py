import pandas as pd

def load_911_data():
    return pd.read_csv("../data/911_calls.csv")

def load_er_data():
    return pd.read_csv("../data/emergency_room_data.csv")

def load_ambulance_data():
    return pd.read_csv("../data/ambulance_response.csv")
