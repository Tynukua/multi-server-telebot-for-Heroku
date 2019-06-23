from flask import Flask, request
import telebot
import os
import json
from requests import post
from random import randint

TOKEN = '834381692:AAGtVWx0RatEgM9GOio-N-fPBc4DqIZBHaM'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
NAME = 'main-server-for-tg'
WORKER = 'not-main-server-for-tg-'
COUNT = 2
i = 0
@app.route(f'/{TOKEN}', methods=['POST'])
def get_updates():
	a = request.stream.read().decode("utf-8")
	#bot.send_message(382572750,a+ str(json.loads(a))	)
	a = json.loads(a)	
	global i
	a = post(f'https://{WORKER}{i+1}.herokuapp.com/{TOKEN}', json = a)
	i = (1+ i)% COUNT
	return "OK", 200


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
