import pyrebase
"""import sqlite3"""
from flask import Flask, render_template, request

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyAqAZIyg2YSVvXCgtqI0b4IGYfp-R88mH8",
    "authDomain": "winter-80fa9.firebaseapp.com",
    "databaseURL": "https://winter-80fa9-default-rtdb.firebaseio.com",
    "projectId": "winter-80fa9",
    "storageBucket": "winter-80fa9.appspot.com",
    "messagingSenderId": "1047783723358",
    "appId": "1:1047783723358:web:0e0aaaae52df428877bfcf",
    "measurementId": "G-XFTNSE9Z2V"
};

firebase = pyrebase.initialize_app(config)
db = firebase.database()
cur_qt = 0
qt = [
    '한식 어때?',
    '다이어트중이야?',
    '매운게 끌려?',
    '누구랑 먹어?',
    '술은? 안드시게? 이걸 참아?'
]
choice = {0: ['O', 'X'], 1: ['O', 'X'], 2: ['O', 'X'], 3: ['X', '혼자', '애인', ' 그외'], 4: ['X', '맥주', '소주']}


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/question')
def question():
    global cur_qt
    cur_qt = (cur_qt + 1) % 5
    return render_template('question.html', question=qt[cur_qt], choices=choice[cur_qt])


@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        data = request.form['data']
        return data
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run()
