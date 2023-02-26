import requests
from dotenv import dotenv_values
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

config = dotenv_values(".env")

TOKEN = config["TOKEN"]
chat_id = config["chat_id"]

# SEND MESSAGE TO PHONE
def sendData(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

async def teleStop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id, text="test")


application = Application.builder().token(TOKEN).build()

application.add_handler(CommandHandler("test", teleStop))
#application.run_polling()
