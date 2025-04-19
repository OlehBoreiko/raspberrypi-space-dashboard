import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Step 1: Get space weather data
url = "http://localhost:5000/donki"
res = requests.get(url)
res.raise_for_status()
data = res.json()

# Step 2: Format summary prompt
prompt = f"""
In the last 5 days:
- {len(data['cme'])} CMEs
- {len(data['flares'])} solar flares
- {len(data['storms'])} geomagnetic storms
"""

# Step 3: Send to ChatGPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a space weather analyst. Write a short summary based on the events listed."},
        {"role": "user", "content": prompt}
    ]
)

# Step 4: Output
print("\n🧠 ChatGPT Solar Activity Summary:\n")
print(response.choices[0].message.content)
