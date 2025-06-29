import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Load env variables
load_dotenv()

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

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hi darling 😘 I'm {BOT_NAME}. Talk to me... 🔥")

# Message handler
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
    await update.message.reply_text("❌ All API keys used up! Try later baby 😢")

# Main app
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

if __name__ == "__main__":
    app.run_polling()
