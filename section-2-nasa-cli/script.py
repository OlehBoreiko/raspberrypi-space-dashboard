import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/planetary/apod"
params = {"api_key": api_key}

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

print(f"📅 Date: {data['date']}")
print(f"📸 Title: {data['title']}")
print(f"📝 Explanation: {data['explanation'][:300]}...")

if data["media_type"] == "image":
    image_url = data["url"]
    image_response = requests.get(image_url, stream=True)
    image_response.raise_for_status()
    with open("apod.jpg", "wb") as f:
        for chunk in image_response.iter_content(1024):
            f.write(chunk)
    print("✅ Image saved as apod.jpg")
else:
    print(f"⚠️ Media is not an image: {data['media_type']}")
