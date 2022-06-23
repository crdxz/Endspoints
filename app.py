from flask import Flask, jsonify, render_template
import pygal 
import json 

app = Flask(__name__)

#1
@app.route("/")
def cadena():
    return "<p>Enviando una cadena de texto...</p>" 
#2
@app.route("/json")
def json():
    return jsonify({"message": "Enviando mensaje con jsonify..."})
#3
@app.route("/books")
def books():
    books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}]
    return jsonify(books)
#4
@app.route("/bar")
def bar():
    line_chart = pygal.Line(width=550, height=350,explicit_size=True)
    line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

    return line_chart.render_response()
#5
@app.route("/render")
def render():
    return render_template('page.html')

if __name__ == "__main__":
    app.run()