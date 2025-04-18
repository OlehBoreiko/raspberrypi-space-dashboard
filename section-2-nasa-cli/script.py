import requests
import os
from datetime import date, timedelta
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

# Use last 5 days for a meaningful dataset
start = (date.today() - timedelta(days=5)).isoformat()
end = date.today().isoformat()

url = "https://api.nasa.gov/neo/rest/v1/feed"
params = {
    "start_date": start,
    "end_date": end,
    "api_key": api_key
}

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

# Extract and flatten all asteroids
rows = []
for day in data["near_earth_objects"]:
    for a in data["near_earth_objects"][day]:
        rows.append({
            "date": day,
            "name": a["name"],
            "diameter_km": a["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
            "velocity_km_s": a["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"],
            "miss_distance_km": float(a["close_approach_data"][0]["miss_distance"]["kilometers"]),
            "hazardous": a["is_potentially_hazardous_asteroid"]
        })

df = pd.DataFrame(rows)
df_hazardous = df[df["hazardous"] == True].sort_values("miss_distance_km")

if df_hazardous.empty:
    print("✅ No potentially hazardous asteroids in the last 5 days!")
else:
    print("⚠️ Dangerous asteroids near Earth (past 5 days):")
    for _, row in df_hazardous.iterrows():
        print("\n🪨 Name:", row["name"])
        print("📅 Date:", row["date"])
        print(f"📏 Max Diameter: {row['diameter_km']:.2f} km")
        print(f"📍 Closest Distance: {row['miss_distance_km']:.0f} km")
        print(f"🚀 Velocity: {float(row['velocity_km_s']):.2f} km/s")
