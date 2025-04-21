# 📬 Build a Telegram Bot for Instant Space Notifications

In this lecture, you’ll create a simple but powerful Telegram bot that sends space-related alerts directly to your phone.

---

## ✅ What’s Included

- `send_message.py`: Fetches ISS flyover data from your local Flask server and sends it to Telegram
- `.env`: Stores your Telegram bot token and chat ID
- Uses `/iss-flyover` route from previous lectures

---

## 📲 Telegram Bot Setup

1. Open Telegram, search for `@BotFather`
2. Send `/newbot` and follow instructions
3. Save the **API token**
4. Start a chat with your bot
5. Visit:
   ```
   https://api.telegram.org/bot<YOUR-TOKEN>/getUpdates
   ```
   Copy the `chat.id` value from the JSON response

---

## 📁 .env File Format

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## 🚀 How to Use

```bash
cd section-6-bonus-gps-telegram
source venv/bin/activate
python send_message.py
```

You should receive a message like:

```
🛰️ ISS Flyover Alert
📆 Rise: 21:12
🌟 Peak: 21:15
📉 Set: 21:18
⏱️ Duration: 360 seconds
```

---

## 💡 Ideas for Expansion

- Send APOD image links daily
- Alert when hazardous asteroids appear
- Trigger via `cron` or `systemd`
- Add user commands like `/neo`, `/iss`, or `/mars`

---

## 🧠 Summary

With this tool, your dashboard becomes interactive. Telegram becomes your real-time cosmic assistant.