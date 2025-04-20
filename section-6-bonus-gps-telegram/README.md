# Track the ISS with Python: Predict Flyovers Using GPS & Skyfield

This project uses your GPS module and the Skyfield astronomy library to compute when the International Space Station (ISS) will pass over your location.

## 📦 Features

- 📍 Reads real-time GPS coordinates from `/dev/ttyACM0`
- 🛰 Downloads and caches ISS TLE data from Celestrak
- 🌍 Calculates upcoming ISS flyovers (rise, peak, set) for the next 2 days
- 🕒 Converts UTC time to local timezone (Kyiv by default)

---

## 🚀 How to Run

1. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install skyfield numpy requests
   ```

3. **Run the script**:
   ```bash
   python iss_flyover.py
   ```

---

## 🔧 Timezone Customization

Edit this line in the script to change the output timezone:
```python
kyiv = ZoneInfo("Europe/Kyiv")
```

Replace `"Europe/Kyiv"` with your own zone from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

---

## 📌 Output Example

```
📍 Location acquired: Latitude = 49.835325, Longitude = 23.879227

📆 Upcoming ISS Flyovers:
2025-04-21 06:19:22 (Kyiv time) — ⬆️ Rise above 10°
2025-04-21 06:22:34 (Kyiv time) — 🌟 Culminate
2025-04-21 06:25:47 (Kyiv time) — ⬇️ Set below 10°
...
```

Each pass includes 3 events:
- ⬆️ Rise — when ISS first becomes visible
- 🌟 Culminate — highest point in the sky
- ⬇️ Set — when ISS disappears under the horizon

---
