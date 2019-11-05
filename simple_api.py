import flask
import numpy as np
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

@app.route('/hello', methods=['POST'])
def send_greeting():
	data = request.get_json()
	if 'name' in data:
		return 'hello, {}\n\n'.format(data['name'])
	else:
		return 'hello mr. no name.\n\n'


@app.route('/secret_word', methods=['POST'])
def find_secret_word():

	text = request.get_json()
	if 'text' in text:
		split_text = text['text'].split()
		secret_word = np.random.choice(split_text)
		return 'the secret word is: {}\n\n'.format(secret_word)
	else:
		return 'sorry. no secret word today.\n\n'
	


