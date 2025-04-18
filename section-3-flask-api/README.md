# Flask API – Raspberry Pi Space Dashboard

This folder contains the base structure for your Flask API server.  
Start here before adding any endpoints.

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

3. Run the Flask server:

```bash
python script.py
```

Visit `http://<raspberry-pi-ip>:5000/` in your browser.

You should see:

```json
{ "message": "Space API is running 🚀" }
```

## 🧱 Files

- `script.py` — your main Flask app
- `requirements.txt` — Python packages
