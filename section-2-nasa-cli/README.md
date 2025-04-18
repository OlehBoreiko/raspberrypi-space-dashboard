# NEO Asteroids Analysis (NASA API)

This script connects to NASA's Near-Earth Object (NEO) API and retrieves data about asteroids that passed near Earth over the last 5 days.

It filters the list to identify those classified as *potentially hazardous* and prints their details in a clean, readable format.

## 🔗 API Endpoint

- https://api.nasa.gov/neo/rest/v1/feed

You will need a free NASA API key to use this script.
Register at: https://api.nasa.gov/

## 🔧 What This Version Does

- Queries asteroid data for the last 5 days
- Filters potentially hazardous objects
- Displays:
  - name
  - date
  - estimated max diameter
  - closest approach distance
  - relative velocity

## ▶️ Run the script

> 💡 **Reminder:** Activate your virtual environment before running:

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
python script.py
```

Expected output (example):

```
🪨 Name: (2023 QZ1)
📅 Date: 2024-04-17
📏 Max Diameter: 0.32 km
📍 Closest Distance: 1450000 km
🚀 Velocity: 18.22 km/s
```

> ✅ If no hazardous asteroids are found, the script will say so clearly.
