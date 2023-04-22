import requests

import json

import time

import telegram

from telegram.ext import Updater, CommandHandler

# Genshin Impact API endpoint

API_ENDPOINT = "https://api.genshin.dev/"

# Telegram Bot token

TOKEN = "your_token_here"

# Create a Telegram Bot instance

bot = telegram.Bot(token=TOKEN)

# Define the /start command handler

def start(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Genshin Impact update bot! You will receive regular updates about the game.")

# Define the /update command handler

def update(update, context):

    # Get the latest game version

    response = requests.get(API_ENDPOINT + "version")

    data = json.loads(response.text)

    latest_version = data["latest_version"]

    # Get the latest game news

    response = requests.get(API_ENDPOINT + "news")

    data = json.loads(response.text)

    latest_news = data[0]

    # Send the latest game version and news to the user

    message = "Latest game version: {}\n\nLatest game news: {}\n\nRead more: {}".format(latest_version, latest_news["title"], latest_news["url"])

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Create an Updater and attach the command handlers

updater = Updater(token=TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CommandHandler('update', update))

# Start the bot

updater.start_polling()

print("Bot started. Press Ctrl+C to stop.")

# Run the bot continuously

while True:

    time.sleep(3600)  # wait 1 hour

    update(None, updater.dispatcher)  # send regular updates to all users

