from flask import Flask, jsonify, render_template, Request
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Main_Page():
    return render_template('home.htm')

@app.route('/sha1=<value>', methods=['GET'])
def Get_Info(value):
    hash = hashlib.sha1(str(value).encode('UTF-8')).hexdigest()
    return jsonify({'Status':'OK', 'Hash': str(hash)})

app.run(debug=True, port=80)