import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Replace YOUR_TOKEN with your Telegram Bot token
bot = telegram.Bot(token=os.environ.get("TELEGRAM_BOT_TOKEN"))

def start(update, context):
    """Handler function for the /start command."""
    message = "Welcome to the Genshin Impact guide! Here you can learn how to play the game and get tips and tricks to improve your gameplay. Type /guide to get started!"
    update.message.reply_text(message)

def guide(update, context):
    """Handler function for the /guide command."""
    message = "To play Genshin Impact on mobile, you can download the game from the App Store or Google Play Store. Once you have the game installed, you can move around using the virtual joystick, jump using the button on the right, and interact with objects using the button on the left.\n\nTo level up your characters, you can use experience materials and ascension materials. Experience materials can be obtained by completing quests and defeating enemies, while ascension materials can be obtained by completing bosses and exploring the world.\n\nFor more tips and tricks, you can visit the official Genshin Impact website at https://genshin.mihoyo.com/en/"
    update.message.reply_text(message)

def echo(update, context):
    """Handler function for all non-command messages."""
    message = "I'm sorry, I don't understand. Type /guide to learn how to play Genshin Impact on mobile!"
    update.message.reply_text(message)

def main():
    """Main function to start the bot."""
    # Create the Updater and pass in the bot's token
    updater = Updater(token=os.environ.get("TELEGRAM_BOT_TOKEN"), use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers for commands and messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("guide", guide))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
