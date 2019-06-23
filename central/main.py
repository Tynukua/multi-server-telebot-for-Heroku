from flask import Flask, request
import os
from requests import post
from random import randint

TOKEN = 'Your token'
app = Flask(__name__)
WORKER_LIST = [] #Names of your apps
COUNT = len(WORKER_LIST)
i = 0
@app.route(f'/{TOKEN}', methods=['POST'])
def get_updates():
	a = request.stream.read().decode("utf-8")
	a = json.loads(a)	
	global i
	a = post(f'https://{WORKER[i]}.herokuapp.com/{TOKEN}', json = a)
	i = (1+ i)% COUNT
	return "OK", 200


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
