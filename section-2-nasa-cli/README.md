# Grab Your NASA API Key & Make Your First Authenticated Request

This example demonstrates how to:

- Register and use a NASA API key
- Store it securely in a `.env` file
- Use `requests` and `python-dotenv` to load it
- Make an authenticated GET request to the APOD endpoint

## 🔧 Setup Instructions

### 1. Copy `.env`:
```bash
cp example.env .env
```

### 2. Paste your API key:
```bash
NASA_API_KEY=your_api_key_here
```

### 3. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 4. Install dependencies:
```bash
pip install requests python-dotenv
```

### 5. Run the script:
```bash
python script.py
```


You should see today’s Astronomy Picture of the Day info printed in the terminal.

---

📌 This example corresponds to the lecture:  
**“Grab Your NASA API Key & Master Python Requests in Minutes”**  from the course **Raspberry Pi Space Dashboard: NASA APIs, Flask & ChatGPT AI**
