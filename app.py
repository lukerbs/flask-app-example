from flask import Flask, render_template

app = Flask(__name__)

# home page
@app.route('/')
def home():
	favorite_food = "pizza"
	return render_template('index.html', food=favorite_food)

# page 2
@app.route('/page_2')
def page_2():
	return render_template('page_2.html')


if __name__ == '__main__':
    # start the app
    app.run(debug=False)