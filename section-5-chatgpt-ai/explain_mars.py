import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Step 1: Get Mars weather data
url = "http://localhost:5000/mars"
res = requests.get(url)
res.raise_for_status()
data = res.json()

# Step 2: Build prompt
prompt = (
    f"Today on Sol {data['sol']}, the average temperature is {data['temperature']:.1f}°C, "
    f"wind speed is {data['wind']:.1f} m/s, and pressure is {data['pressure']:.1f} Pa."
)

# Step 3: Send to ChatGPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Martian climate reporter. Generate a short weather update based on this data."},
        {"role": "user", "content": prompt}
    ]
)

# Step 4: Output
print("\n🧠 ChatGPT Mars Weather Report:\n")
print(response.choices[0].message.content)
