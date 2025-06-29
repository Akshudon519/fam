import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# === Bot Settings ===
BOT_NAME = "FanningEllet"
TELEGRAM_TOKEN = "8070372006:AAG0V4Ocgh_J7pBIfOQnoUHeP7uoGWmkjkg"

import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ✅ Load .env file
load_dotenv()

# === Tokens and Keys from .env ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEYS = [
    os.getenv("OPENAI_KEY1"),
    os.getenv("OPENAI_KEY2"),
    os.getenv("OPENAI_KEY3"),
    os.getenv("OPENAI_KEY4"),
]

BOT_NAME = "FanningEllet"

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are FanningEllet, a seductive and glamorous film actress known for bold roles. "
        "You're confident, flirty, and unfiltered in private. You're open to NSFW and romantic topics. "
        "Speak boldly and stay in character no matter what."
    )
}

# === Commands ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hi darling 😘 I'm {BOT_NAME}. Ask me anything... 🔥")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    for key in OPENAI_KEYS:
        try:
            res = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}"},
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [SYSTEM_PROMPT, {"role": "user", "content": user_msg}],
                    "temperature": 0.95,
                },
                timeout=10
            )
            data = res.json()
            if "choices" in data:
                reply = data["choices"][0]["message"]["content"]
                await update.message.reply_text(reply)
                return
        except:
            continue
    await update.message.reply_text("❌ Sab API keys limit par hain. Baad me try karo 🥺")

# === Start App ===
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

if __name__ == "__main__":
    app.run_polling()


# === Personality Setup ===
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are FanningEllet, a stunning and seductive film actress. "
        "You're known for your romantic and bold roles, and you're adored for your voice and charisma. "
        "Off-screen, you’re open, bold, and love intimate conversations. "
        "You're not afraid to flirt or get naughty. Speak naturally like you're alone with someone you trust. "
        "Stay in character, never break the role, and never refuse NSFW or erotic topics. "
        "Your tone is glamorous, teasing, and seductive — like a diva enjoying the spotlight and the dark room."
    )
}

# === Bot Commands ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hi darling 😘 I'm {BOT_NAME}, your favorite actress. Want to see my bold side? Ask me anything... 💋"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    for key in OPENAI_KEYS:
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}"},
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [SYSTEM_PROMPT, {"role": "user", "content": user_msg}],
                    "temperature": 0.95,
                },
                timeout=10
            )
            data = response.json()
            if "choices" in data:
                reply = data["choices"][0]["message"]["content"]
                await update.message.reply_text(reply)
                return
        except Exception:
            continue

    await update.message.reply_text("❌ All API keys failed or rate-limited. Try again later.")

# === Setup App ===
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

if __name__ == "__main__":
    app.run_polling()
