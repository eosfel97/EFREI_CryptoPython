from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                   

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt', methods=['POST'])
def encryptage():
    data = request.get_json()
    cle = data.get('cle')
    valeur = data.get('valeur')
    f = Fernet(cle)
    token = f.encrypt(valeur.encode())
    return jsonify({"result": token.decode()})

@app.route('/decrypt', methods=['POST'])
def decryptage():
    data = request.get_json()
    cle = data.get('cle')
    token = data.get('token')
    f = Fernet(cle)
    valeur = f.decrypt(token.encode()).decode()
    return jsonify({"result": valeur})

if __name__ == "__main__":
    app.run(debug=True)
