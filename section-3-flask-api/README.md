# Flask API – NASA Space Dashboard

This Flask app serves live space data from NASA and other public APIs.  
You can use it as a backend for your own dashboard or IoT device.

## 🚀 How to Run

1. Activate your virtual environment:

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         	# Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
python script.py
```

Visit `http://<raspberry-pi-ip>:5000/` to check the API is running.

## 📡 Available Endpoints

| Route       | Description                                      |
|-------------|--------------------------------------------------|
| `/`         | Root check – returns a "Space API is running 🚀" message |
| `/iss`      | Returns current location of the ISS              |
| `/neo`      | Returns a list of potentially hazardous asteroids (past 5 days) |
| `/mars`     | Returns latest archived Mars weather from InSight |
| `/donki`    | Returns recent space weather events (CME, flares, storms) *(cached)* |
| `/apod`     | Returns Astronomy Picture of the Day *(cached, error-handled)* |

All endpoints return JSON data and can be tested via browser, Postman, or curl.

## ⚡ Built-In Caching

The `/apod` and `/donki` routes use in-memory caching (TTL = 5 minutes):

- Speeds up repeat requests
- Reduces traffic to NASA API
- Avoids hitting API rate limits

### ⏱ Test with curl:

```bash
time curl http://localhost:5000/apod
```

First request: slower (fetches from NASA)  
Second request: instant (served from cache)

## 🛠 Logging & Error Handling

- Every route using external APIs is wrapped in `try-except` blocks.
- If NASA is unavailable or the key is wrong, you’ll get:

```json
{ "error": "Failed to fetch APOD" }
```

- Flask logs the exact error to terminal:
```
APOD API failed: 403 Client Error: Forbidden
```

### 🧪 Simulate a failure:

1. Open your `.env` file and change `NASA_API_KEY=BADKEY123`
2. Restart the Flask server
3. Wait a few seconds (or change `CACHE_DURATION` to a low number)
4. Run:

```bash
curl http://localhost:5000/apod
```

✅ You’ll get an error message in JSON and a clear log in terminal — no crash.

## 🧱 Project Files

- `script.py` – your Flask app
- `requirements.txt` – required packages
