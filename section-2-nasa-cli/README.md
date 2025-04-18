# Solar Activity Monitor (NASA DONKI API)

This script connects to NASA's DONKI API and retrieves data about recent space weather events:

- ☀️ Coronal Mass Ejections (CME)
- 🔆 Solar Flares (FLR)
- 🌍 Geomagnetic Storms (GST)

## 🔗 API Endpoints

Base URL: https://api.nasa.gov/DONKI  
- CME: /CME  
- FLR: /FLR  
- GST: /GST

## 🧪 What This Version Does

- Queries events from the last 5 days
- Makes 3 separate API requests
- Displays relevant details for each event
- Outputs clear messages if no events found

## ▶️ Run the script

> 💡 **Reminder:** Activate your virtual environment before running:

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
python script.py
```

Example output:

```
☀️ CME Events

Date: 2024-04-17
Catalog: SWRC_CATALOG
Note: Fast CME detected heading west

🔆 Solar Flares

Date: 2024-04-16
Class: M1.1
Active Region: 3632

🌍 Geomagnetic Storms

Date: 2024-04-18
G-Level: G2
```

> ✅ If there are no events for a given type, the script will say so.
