import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
key = os.getenv("NASA_API_KEY")

# Define endpoint and parameters
url = "https://api.nasa.gov/planetary/apod"
params = {"api_key": key}

# Send request
response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

# Output selected data
print(f"Title: {data['title']}")
print(f"Date: {data['date']}")
print(f"Explanation: {data['explanation'][:200]}...")
