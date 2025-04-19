# ChatGPT Asteroid Risk Summary

This script fetches data from your local `/neo` Flask API route and sends it to OpenAI's ChatGPT to generate a natural-language summary.

## 🔧 Setup

1. Activate your virtual environment:
```bash
source venv/bin/activate
```

2. Install the required libraries:
```bash
pip install openai python-dotenv requests
```

3. Create a `.env` file based on the example:
```env
OPENAI_API_KEY=your_api_key_here
```

## 📄 What the Script Does

1. Sends a GET request to `http://localhost:5000/neo`
2. Collects a list of hazardous asteroids
3. Formats the list into lines like:
```
2025-04-20 – (2024 AB12) (0.24 km, 21.9 km/s)
```
4. Sends that formatted list to ChatGPT with the prompt:
> "You are a space analyst. Summarize asteroid risk."

5. Prints the response in the terminal.

## 🚀 Run the Script

```bash
python explain_neo.py
```

You’ll get a result like:
> “5 hazardous asteroids will pass near Earth this week. The largest is 270 meters wide...”

