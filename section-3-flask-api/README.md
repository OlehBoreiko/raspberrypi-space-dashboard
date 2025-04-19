# Flask API – NASA Space Dashboard

This Flask app serves live space data from NASA and other public APIs.  
You can use it as a backend for your own dashboard or IoT device.

## 🚀 How to Run

1. Activate your virtual environment:

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows
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

## ⚡ Built-In Caching

The `/apod` and `/donki` routes use in-memory caching (TTL = 5 minutes) to improve speed and reduce API usage.

## 🛠 Logging & Error Handling

- Logs cache usage and API call success/failure
- Handles API errors with `try-except` and returns JSON errors instead of crashing

## ✅ Testing the API

### 1. Curl (manual test)

```bash
curl http://raspberry-pi-ip:5000/apod
```

or measure speed:

```bash
time curl http://raspberry-pi-ip:5000/apod
```

### 2. Postman (GUI test)

- Open Postman and make a GET request to `http://raspberry-pi-ip:5000/neo`
- See the JSON response, headers, status code

### 3. Pytest (automated test)

Install pytest if needed:

```bash
pip install pytest
```

Run the test suite:

```bash
pytest
```

Tests are defined in `test_app.py`. They verify:
- Status code is 200
- Response is JSON
- Homepage contains “Space API”

## 🧱 Project Files

- `script.py` – your Flask app
- `test_app.py` – test script using Pytest
- `requirements.txt` – required packages

## 🚀 Deployment Tips

You can move this project to another Raspberry Pi or server easily.

### On the new device:

1. Clone or copy the folder
2. Create a new virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your `.env` file with a valid NASA_API_KEY
5. Start the app:

```bash
python script.py
```

✅ Flask will show a message:
```
WARNING: This is a development server. Do not use it in a production deployment.
```
That’s okay! For Raspberry Pi and testing, this is fine.

In Section 7, we’ll show you how to launch it on boot using `systemd` for 24/7 operation.
