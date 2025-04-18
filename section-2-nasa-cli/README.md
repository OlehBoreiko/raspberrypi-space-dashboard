# Astronomy Picture of the Day (NASA APOD API)

This script fetches the latest Astronomy Picture of the Day from NASA's APOD API and saves the image locally.

## 🔗 API Endpoint

- https://api.nasa.gov/planetary/apod

## 🧪 What This Version Does

- Retrieves the daily photo with metadata
- Displays:
  - Date
  - Title
  - First 300 characters of the explanation
- Saves the image locally if it's a photo
- Handles cases when the media is not an image

## ▶️ Run the script

> 💡 **Reminder:** Activate your virtual environment before running:

```bash
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
python script.py
```

Example output:

```
📅 Date: 2024-04-19
📸 Title: Starburst Galaxy M94
📝 Explanation: M94 is a stunning galaxy with a very bright core...
✅ Image saved as apod.jpg
```

> ⚠️ If the media is a video or not an image, the script will notify you.
