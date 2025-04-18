# Mars Weather Snapshot (NASA InSight API)

This script connects to NASA's archived InSight Mars Weather API and displays historical climate data from the Red Planet.

## 🔗 API Endpoint

- https://api.nasa.gov/insight_weather/
- Note: This API is archived and not updated beyond 2022.

## 🧪 What This Version Does

- Loads your API key from .env
- Queries the most recent available Martian sol
- Displays:
  - Sol number
  - Average temperature (°C)
  - Average wind speed (m/s)
  - Average pressure (Pa)

## ▶️ Run the script

> 💡 **Reminder:** Activate your virtual environment before running:

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
python script.py
```

Expected output:

```
📅 Sol: 681
🌡 Avg Temperature: -65.0 °C
🌬 Wind Speed: 4.8 m/s
📈 Pressure: 734.1 Pa
```

> ✅ If the API returns no data, the script will exit cleanly.
