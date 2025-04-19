# ChatGPT AI Tools (Section 5)

This folder contains ready-made scripts for generating summaries using OpenAI’s GPT models based on your Flask API data.

---

## 📁 Scripts

### ✅ explain_neo.py
Summarizes potentially hazardous asteroids using data from `/neo`.

### ✅ explain_donki.py
Summarizes solar activity (CMEs, flares, storms) using data from `/donki`.

---

## 🔧 Setup Instructions

1. Activate your Python virtual environment:
```bash
source venv/bin/activate
```

2. Install required packages:
```bash
pip install openai python-dotenv requests
```

3. Create a `.env` file using the example provided:
```env
OPENAI_API_KEY=your_api_key_here
```

---

## 🚀 Run Scripts

### Asteroid Summary
```bash
python explain_neo.py
```

### Solar Activity Summary
```bash
python explain_donki.py
```

Each script will output a ChatGPT-generated summary based on real-time data from your Flask API.
