from flask import Flask, jsonify, render_template, Request, send_file
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Main_Page():
    return render_template('home.htm')

@app.route('/sha1=<value>', methods=['GET'])
def Get_Info(value):
    hash = hashlib.sha1(str(value).encode('UTF-8')).hexdigest()
    return jsonify({'Status':'OK', 'Hash': str(hash)})

@app.route('/sha256=<value>', methods=['GET'])
def SHA256(value):
    hash = hashlib.sha256(str(value).encode('UTF-8')).hexdigest()
    return jsonify({'Status': 'OK', 'Hash': str(hash)})

@app.route('/sha512=<value>', methods=['GET'])
def SHA512(value):
    hash = hashlib.sha512(str(value).encode('UTF-8')).hexdigest()
    return jsonify({'Status': 'OK', 'Hash': str(hash)})

@app.route('/download/platform=<value>', methods=['GET'])
def Download_File(value):
    if value == "win":
        return send_file(open('/root/payload.exe', 'rb'))
    #elif value == "liunx":
        #return send_file(open('/root/payload', 'r'))
    else:
        return jsonify({'Platform Not Found': 404})

@app.route('/updates/version=<value>', methods=['GET'])
def Check_API(value):
    if int(value) > 1.0:
        return jsonify({'update_url': ''})
    else:
        return jsonify{'update_url': 'update'} 

app.run(debug=True, port=80, host='0.0.0.0')
