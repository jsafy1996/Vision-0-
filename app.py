from flask import Flask, render_template, jsonify
import json
from additional_backend import data_processing

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.route('/2')
def hello():
    return render_template('index.html')


@app.route('/do/<coords>')
def doStuff(coords):
    print(coords)
    #data_processing.fix_database()
    coords = data_processing.stuff(coords)
    return jsonify(coords)

if(__name__ == '__main__'):
    app.run(debug=True)