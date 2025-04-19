import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Step 1: Get asteroid data from local API
neo_url = "http://localhost:5000/neo"
response = requests.get(neo_url)
response.raise_for_status()
neos = response.json()["hazardous_asteroids"]

# Step 2: Format data into a readable list
summary = "\n".join([
    f"{obj['date']} – {obj['name']} ({obj['diameter_km']:.2f} km, {obj['velocity_kms']:.1f} km/s)"
    for obj in neos
])

# Step 3: Call ChatGPT using the OpenAI Python SDK (v1+)
chat_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a space analyst. Summarize asteroid risk."},
        {"role": "user", "content": f"Here is the data:\n{summary}"}
    ]
)

# Step 4: Output response
print("\n🧠 ChatGPT Asteroid Risk Summary:\n")
print(chat_response.choices[0].message.content)
