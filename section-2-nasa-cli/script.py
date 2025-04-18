import requests
import time
from datetime import datetime, timezone

URL = "http://api.open-notify.org/iss-now.json"

def fetch_iss_position():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    pos = data["iss_position"]
    timestamp = data["timestamp"]
    return {
        "timestamp": datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat(),
        "latitude": pos["latitude"],
        "longitude": pos["longitude"]
    }

if __name__ == "__main__":
    for _ in range(3):
        position = fetch_iss_position()
        print(f"{position['timestamp']} → lat: {position['latitude']} | lon: {position['longitude']}")
        time.sleep(5)
