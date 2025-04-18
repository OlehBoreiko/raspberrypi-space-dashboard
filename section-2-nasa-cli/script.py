import requests
import os
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

BASE = "https://api.nasa.gov/DONKI"
start_date = (date.today() - timedelta(days=5)).isoformat()
end_date = date.today().isoformat()

def fetch(endpoint):
    url = f"{BASE}/{endpoint}"
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# CME Events
print("☀️ CME Events")
cmes = fetch("CME")
if not cmes:
    print("✅ No CME events in the last 5 days.")
else:
    for cme in cmes:
        print(f"\nDate: {cme.get('startTime')}")
        print(f"Catalog: {cme.get('catalog') or '(not specified)'}")
        print(f"Note: {cme.get('note') or '(no note)'}")

# Solar Flares
print("\n🔆 Solar Flares")
flares = fetch("FLR")
if not flares:
    print("✅ No solar flares detected.")
else:
    for flare in flares:
        print(f"\nDate: {flare.get('beginTime')}")
        print(f"Class: {flare.get('classType')}")
        print(f"Active Region: {flare.get('activeRegionNum')}")

# Geomagnetic Storms
print("\n🌍 Geomagnetic Storms")
storms = fetch("GST")
if not storms:
    print("✅ No geomagnetic storms recorded.")
else:
    for gst in storms:
        print(f"\nDate: {gst.get('startTime')}")
        if gst.get("allKpIndex"):
            kp = gst["allKpIndex"][0]
            print(f"G-Level: {kp.get('kpIndex')}")
        else:
            print("G-Level: (not available)")
