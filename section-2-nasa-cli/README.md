# Section 2: NASA APIs – Accessing Real-Time Space Data

In this section, we explore how to access real-time space data using various NASA APIs and Python. We progressively add functionality to a single `script.py` file to build a powerful data retrieval tool for Raspberry Pi.

## What You Will Learn
- How to retrieve the real-time location of the International Space Station (ISS)
- How to track Near-Earth Objects (asteroids) with NASA's NEO API
- How to monitor space weather events like solar flares and geomagnetic storms
- How to get the latest weather data from Mars
- How to download the Astronomy Picture of the Day (APOD)

Each API interaction is built step-by-step, with clean, well-commented code.

---

## Overview of API Integrations

### 🚀 ISS Data (`iss-data`)
- Retrieve the current position of the International Space Station (latitude, longitude, timestamp).
- Understand JSON structure and basic API calls.

### ☄️ Near-Earth Object Data (`neo-data`)
- Query information about asteroids approaching Earth.
- Learn how to work with date ranges and parse detailed JSON responses.

### 🌞 Space Weather Data (`donki-data`)
- Access data about solar activity (CMEs, solar flares, and geomagnetic storms).
- Practice working with multiple types of events and dynamic API queries.

### 🔴 Mars Weather Data (`mars-weather`)
- Retrieve recent weather reports from Mars using NASA's InSight mission API.
- Learn to handle different data fields such as temperature, wind, and pressure.

### 📸 Astronomy Picture of the Day (`apod-photo`)
- Download and display NASA's daily featured space image.
- Learn to handle both image and text data in a single API response.

---

## File Structure
```
/section-2-nasa-apis/
│
├── script.py          # Unified Python script for all API interactions
└── README.md          # This overview file
```

---

## Requirements
- Python 3.x
- `requests` library

Install required package:
```bash
pip install requests
```

---

## Notes
- All API examples are designed to be simple and educational.
- No API key is required for the APIs used in this section (at the time of creation).
- Always check the NASA API documentation for updates.

---
