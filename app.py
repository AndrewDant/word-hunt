from flask import Flask, render_template, request
import ai_functions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/word-hunt", methods=["POST"])
def word_hunt():
    user_input = request.form['wordDescription']
    response = ai_functions.word_hunt_query(user_input)
    return render_template('index.html', response=response)
