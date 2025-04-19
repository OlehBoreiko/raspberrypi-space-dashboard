from flask import Flask, jsonify, render_template
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import date, timedelta
import time

load_dotenv()
client = OpenAI()
api_key = os.getenv("NASA_API_KEY")

app = Flask(__name__)

# Simple in-memory cache
cache = {}
CACHE_DURATION = 2  # seconds (5 minutes)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iss")
def iss():
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    res.raise_for_status()
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
    res.raise_for_status()
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
    res.raise_for_status()
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
    now = time.time()
    if "donki" in cache and now - cache["donki"]["timestamp"] < CACHE_DURATION:
        return jsonify(cache["donki"]["data"])

    today = date.today()
    start = (today - timedelta(days=5)).isoformat()
    end = today.isoformat()
    base = "https://api.nasa.gov/DONKI"
    def fetch(endpoint):
        res = requests.get(f"{base}/{endpoint}?startDate={start}&endDate={end}&api_key={api_key}")
        return res.json()
    data = {
        "cme": fetch("CME"),
        "flares": fetch("FLR"),
        "storms": fetch("GST")
        }
    cache["donki"] = {"data": data, "timestamp": now}
    return jsonify(data)

@app.route("/apod")
def apod():
    now = time.time()
    if "apod" in cache and now - cache["apod"]["timestamp"] < CACHE_DURATION:
        app.logger.info("APOD cache HIT")
        return jsonify(cache["apod"]["data"])

    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        output = {
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"][:300],
            "url": data["url"]
        }
        cache["apod"] = {"data": output, "timestamp": now}
        app.logger.info("APOD cache MISS → updated")
        return jsonify(output)

    except Exception as e:
        app.logger.error(f"APOD API failed: {e}")
        return jsonify({"error": "Failed to fetch APOD"}), 500


@app.route("/ai/neo", methods=["POST"])
def ai_neo():
    try:
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={(date.today() - timedelta(days=5)).isoformat()}&end_date={date.today().isoformat()}&api_key={api_key}"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        neos = []
        for day in data["near_earth_objects"]:
            for neo in data["near_earth_objects"][day]:
                if neo["is_potentially_hazardous_asteroid"]:
                    neos.append(f"{day} – {neo['name']} ({neo['estimated_diameter']['kilometers']['estimated_diameter_max']:.2f} km, {float(neo['close_approach_data'][0]['relative_velocity']['kilometers_per_second']):.1f} km/s)")
        summary = "\n".join(neos)
        prompt = f"Summarize this asteroid risk:\n{summary}"
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a space analyst. Summarize asteroid risk based on the following list."},
                {"role": "user", "content": prompt}
            ]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Error: {e}", 500

@app.route("/ai/donki", methods=["POST"])
def ai_donki():
    try:
        url = f"https://api.nasa.gov/DONKI/CME?startDate={(date.today() - timedelta(days=5)).isoformat()}&endDate={date.today().isoformat()}&api_key={api_key}"
        cme = requests.get(url).json()
        flr = requests.get(f"https://api.nasa.gov/DONKI/FLR?startDate={(date.today() - timedelta(days=5)).isoformat()}&endDate={date.today().isoformat()}&api_key={api_key}").json()
        gst = requests.get(f"https://api.nasa.gov/DONKI/GST?startDate={(date.today() - timedelta(days=5)).isoformat()}&endDate={date.today().isoformat()}&api_key={api_key}").json()
        prompt = f"In the last 5 days:\n- {len(cme)} CMEs\n- {len(flr)} flares\n- {len(gst)} geomagnetic storms"
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a space weather analyst. Write a short summary based on this:"},
                {"role": "user", "content": prompt}
            ]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Error: {e}", 500

@app.route("/ai/mars", methods=["POST"])
def ai_mars():
    try:
        url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        sol = data["sol_keys"][-1]
        weather = data[sol]
        prompt = f"Today on Sol {sol}, the average temperature is {weather['AT']['av']}°C, wind is {weather['HWS']['av']} m/s, pressure is {weather['PRE']['av']} Pa."
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Martian weather reporter. Turn this data into a short summary."},
                {"role": "user", "content": prompt}
            ]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Error: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
