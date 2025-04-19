# Section 4 – Flask-Powered Web Dashboard

This folder contains a self-contained version of your Raspberry Pi Space Dashboard, with both the frontend (HTML/CSS/JS) and backend (Flask API) in one place.

## 📁 Folder Structure

```
section-4-web-dashboard/
├── script.py               ← Flask server and API routes
├── templates/
│   └── index.html          ← Dashboard HTML layout served by Flask
├── static/
│   ├── style.css           ← Tailwind styles (customizable)
│   └── script.js           ← JavaScript logic (fetch calls will be added in later lectures)
```

## ⚙️ How It Works

We created a copy of `script.py` directly in this folder. This way, you don’t need to run Flask from another location or reference template/static folders manually.

This file already includes:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

This allows Flask to serve the HTML UI from the `templates/` folder and static assets from `static/`.

## 🔧 Setup Instructions

1. Activate your virtual environment (if not active):

```bash
source venv/bin/activate
```

2. From inside `section-4-web-dashboard/`, run the Flask server:

```bash
python script.py
```

3. In your browser, visit:

```
http://<your-raspberry-pi-ip>:5000
```

You should see the styled dashboard UI.

## 📌 JavaScript Integration

In `script.js`, you don’t need to hardcode IPs. Use relative paths like:

```javascript
fetch("/iss")
```

We’ll begin writing real fetch logic in next lectures.
