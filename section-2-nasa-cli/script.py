import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/insight_weather/"
params = {
    "api_key": api_key,
    "feedtype": "json",
    "ver": "1.0"
}

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

sols = data.get("sol_keys", [])
if not sols:
    print("❌ No data available from the InSight API.")
    exit()

latest_sol = sols[-1]
mars = data[latest_sol]

print(f"📅 Sol: {latest_sol}")
print(f"🌡 Avg Temperature: {mars['AT']['av']} °C")
print(f"🌬 Wind Speed: {mars['HWS']['av']} m/s")
print(f"📈 Pressure: {mars['PRE']['av']} Pa")
