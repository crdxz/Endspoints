from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<p>Hello, World!</p>" 
@app.route("/goodbye")
def bye_world():
    return "<p>Good bye, World!</p>" 


