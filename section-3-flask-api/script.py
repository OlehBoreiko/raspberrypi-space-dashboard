from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Space API is running 🚀"})

@app.route("/iss")
def iss():
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    data = res.json()
    position = data["iss_position"]
    return jsonify({
        "timestamp": data["timestamp"],
        "latitude": position["latitude"],
        "longitude": position["longitude"]
    })

@app.route("/neo")
def neo():
    end = date.today()
    start = end - timedelta(days=5)
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start}&end_date={end}&api_key={api_key}"
    res = requests.get(url)
    data = res.json()
    neos = []
    for day in data["near_earth_objects"]:
        for neo in data["near_earth_objects"][day]:
            if neo["is_potentially_hazardous_asteroid"]:
                neos.append({
                    "name": neo["name"],
                    "date": day,
                    "diameter_km": neo["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    "distance_km": float(neo["close_approach_data"][0]["miss_distance"]["kilometers"]),
                    "velocity_kms": float(neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"])
                })
    return jsonify({"hazardous_asteroids": neos})


@app.route("/mars")
def mars():
    url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
    res = requests.get(url)
    data = res.json()
    sols = data.get("sol_keys", [])
    if not sols:
        return jsonify({"error": "No data available"})
    latest = sols[-1]
    weather = data[latest]
    return jsonify({
        "sol": latest,
        "temperature": weather["AT"]["av"],
        "wind": weather["HWS"]["av"],
        "pressure": weather["PRE"]["av"]
    })

@app.route("/donki")
def donki():
    today = date.today()
    start = (today - timedelta(days=5)).isoformat()
    end = today.isoformat()
    base = "https://api.nasa.gov/DONKI"
    def fetch(endpoint):
        res = requests.get(f"{base}/{endpoint}?startDate={start}&endDate={end}&api_key={api_key}")
        return res.json()
    return jsonify({
        "cme": fetch("CME"),
        "flares": fetch("FLR"),
        "storms": fetch("GST")
    })

@app.route("/apod")
def apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    res = requests.get(url)
    data = res.json()
    return jsonify({
        "title": data["title"],
        "date": data["date"],
        "explanation": data["explanation"][:300]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
