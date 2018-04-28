from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.route('/do/<coords>')
def doStuff(coords):
    print(coords)
    #print(json.loads(coords))

    return jsonify({'coords':'hello world'})

if(__name__ == '__main__'):
    app.run(debug=True)