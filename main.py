import telegram
import time
import requests
from flask import Flask, request

# Enter your Telegram bot token here
TOKEN = '5915413280:AAGQbYmJm-TI-N76ElacXWLg5OJqyJKsEmw'

# Set up the Flask app
app = Flask(__name__)
bot = telegram.Bot(token=TOKEN)

# Define a route for handling incoming webhook updates
@app.route('/telegram_webhook', methods=['POST'])
def telegram_webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.effective_chat.id
    
    # Send a request to the Genshin Impact API for the latest news
    response = requests.get('https://genshin.mihoyo.com/en/news/detail/12345')
    if response.status_code == 200:
        # Parse the HTML response to extract the news title and content
        news_title = response.json()['data']['title']
        news_content = response.json()['data']['content']
        
        # Compose a message with the news title and content
        message = f'**New update for Genshin Impact:**\n\n{news_title}\n\n{news_content}'
        
        # Send the message to the user who sent the message to the bot
        bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=telegram.ReplyKeyboardRemove())
    
    return 'OK'

# Set up the webhook URL
webhook_url = 'https://your-app-name.onrender.com/telegram_webhook'
bot.setWebhook(webhook_url)

# Start the Flask app
if __name__ == '__main__':
    app.run(port=5000)
