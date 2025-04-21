import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_telegram_message(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("⚠️ Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")
        return
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    res = requests.post(API_URL, data=payload)
    if res.ok:
        print("✅ Message sent!")
    else:
        print("❌ Failed to send message:", res.text)

def get_iss_flyover():
    try:
        res = requests.get("http://localhost:5000/iss-flyover")
        data = res.json()
        if "error" in data:
            return "⚠️ ISS Flyover data unavailable"
        return (
            f"🛰️ *ISS Flyover Alert*\n"
            f"📆 Rise: {data['rise']}\n"
            f"🌟 Peak: {data['peak']}\n"
            f"📉 Set: {data['set']}\n"
            f"⏱️ Duration: {data['duration_seconds']} seconds"
        )
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    message = get_iss_flyover()
    send_telegram_message(message)