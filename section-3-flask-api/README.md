# Flask API – NASA Space Dashboard

This Flask app serves live space data from NASA and other public APIs.  
You can use it as a backend for your own dashboard or IoT device.

## 🚀 How to Run

1. Activate your virtual environment:

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
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
| `/donki`    | Returns recent space weather events (CME, flares, storms) |
| `/apod`     | Returns Astronomy Picture of the Day title, date, and explanation |

All endpoints return JSON data and can be tested via browser, Postman, or curl.

## 🧱 Project Files

- `script.py` – your Flask app
- `requirements.txt` – required packages
