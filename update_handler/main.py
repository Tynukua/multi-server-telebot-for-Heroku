from flask import Flask, request
import telebot
import os
import json
from requests import post
TOKEN = '834381692:AAGtVWx0RatEgM9GOio-N-fPBc4DqIZBHaM'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def getMessage():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Hello2, ' + message.from_user.first_name)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
