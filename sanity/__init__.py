import os

from flask import Flask

def create_app(test_confi=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	
	# the simplest homepage
	@app.route('/')
	def index():
		return 'Sanity Home'
	
	return app
