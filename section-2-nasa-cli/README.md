# ISS Tracker (Open API)

This version of the script connects to a free, public API that returns the current position of the International Space Station (ISS) in real time.

## 🔗 API Endpoint

- http://api.open-notify.org/iss-now.json  
  _Note: This is not an official NASA API._

## 🧪 What This Version Does

- Sends a GET request to fetch ISS location
- Extracts `timestamp`, `latitude`, and `longitude`
- Displays the data in the terminal, every 5 seconds (3 times)

## ▶️ Run the script

> 💡 **Reminder:** Before running the script, make sure your virtual environment is activated.  
> Otherwise, some packages might not be available.

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows
python script.py
```

Expected output (example):

```
2024-04-20T12:00:00+00:00 → lat: 48.123 | lon: -123.456
...
```

> 💡 Make sure to save the file before running!
