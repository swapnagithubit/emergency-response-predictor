from flask import Flask, request, jsonify
from predict import predict_emergency
from nearest_service import find_nearest

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    description = data["description"]
    lat = data["lat"]
    lon = data["lon"]

    emergency_type = predict_emergency(description)

    if emergency_type == "EMS":
        service = find_nearest(lat, lon, "hospital")

    elif emergency_type == "Fire":
        service = find_nearest(lat, lon, "fire")

    else:
        service = find_nearest(lat, lon, "police")

    return jsonify({
        "emergency_type": emergency_type,
        "nearest_service": service["name"],
        "contact": service["phone"]
    })

if __name__ == "__main__":
    app.run(debug=True)
