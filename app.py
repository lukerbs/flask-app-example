from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	name = 'Luke'
	return render_template('index.html', name=name)
