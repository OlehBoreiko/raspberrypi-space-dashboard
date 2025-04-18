# Raspberry Pi Space Dashboard

🌌 **Build a Space Dashboard on Raspberry Pi using NASA APIs, Flask, and ChatGPT AI!**

## 🚀 About the Project

This repository contains the code and resources for the Udemy course:  
**"Raspberry Pi Space Dashboard: NASA APIs, Flask & ChatGPT AI"**

You'll learn how to:

- Interact with NASA's powerful space APIs (ISS, NEO, Mars, DONKI, APOD).
- Develop RESTful APIs using Flask on Raspberry Pi.
- Integrate frontend dashboards with real-time API data.
- Enhance your app with ChatGPT-powered AI explanations.
- Automate deployment using systemd, cron, and more.

---

## 📚 Course Structure

| Section | Description                                 |
|---------|---------------------------------------------|
| 1       | Raspberry Pi Initial Setup                  |
| 2       | CLI Python scripts to fetch NASA data       |
| 3       | Build a Flask REST API                      |
| 4       | Web Dashboard with HTML/CSS/JS              |
| 5       | Enhance with ChatGPT AI insights            |
| 6       | Bonus: GPS module & Telegram notifications  |
| 7       | Deployment and systemd automation           |

---

## ⚙️ Getting Started

### 1. Clone the repo:
```bash
git clone https://github.com/OlehBoreiko/raspberrypi-space-dashboard.git
cd raspberrypi-space-dashboard
```

### 2. Set up virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure your API keys:
Copy **example.env** to **.env** and fill in your NASA and OpenAI API keys.
```bash
NASA_API_KEY=your_nasa_key_here
OPENAI_API_KEY=your_openai_key_here
```

### 4. Run scripts and examples:
Navigate through tagged lectures for guided steps:
```bash
git checkout tags/sec2-api-basics
python script.py
```

🌟 Udemy Course Link
Enroll in the full Udemy course here:
➡️ [Udemy course URL]