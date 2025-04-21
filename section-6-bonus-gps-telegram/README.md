# 🛰️ Display ISS Flyover Times in Your Space Dashboard

In this lecture, we implemented a unified ISS Tracker block that shows both the real-time position of the International Space Station and upcoming flyover times for the user's location.

---

## ✅ Features Implemented

- `/iss` route – gets real-time ISS position from Open Notify API
- `/iss-flyover` route – computes the next visible pass of the ISS over your location using Skyfield + TLE data
- `/ai/iss-tracker` – AI explanation based on live flyover data (ChatGPT API)
- `get_gps_coordinates()` – with fallback to hardcoded coordinates if GPS module is missing
- Unified `🛰️ ISS Tracker` block in `index.html`
- Tailwind CSS layout with icons: 📍 Current Position and 📆 Next Flyover
- Button to refresh data manually
- 🧠 Explain with AI button for educational support

---

## 🧭 Files in this folder

- `script.py` – Flask backend for all routes and AI
- `index.html` – Dashboard UI with ISS Tracker block
- `script.js` – Handles dynamic updates for ISS position + flyover data

---

## 🔧 How to Run

```bash
cd section-6-bonus-gps-telegram
source venv/bin/activate
python script.py
```

Open `http://<your-pi-ip>:5000` in your browser.

---

## 🧠 Note for Students Without GPS Module

In `script.py`, if you don’t have a GPS module, the app will automatically use fallback coordinates (Kyiv by default). You can edit these in the `get_gps_coordinates()` function.

---

## 💡 Sample Flyover Output

```json
{
  "rise": "2025-04-21 06:19:22",
  "peak": "2025-04-21 06:22:34",
  "set": "2025-04-21 06:25:47",
  "duration_seconds": 385
}
```

---

## 🧠 AI Example Prompt

The AI uses real-time flyover data to explain:
> "The ISS will rise at 06:19:22, reach its highest point at 06:22:34, and set at 06:25:47. Here's what that means..."

---

## 🚀 Summary

With this lecture, the dashboard becomes a smart observation assistant for space enthusiasts.