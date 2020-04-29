from flask import Flask, session
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    session['username'] = 'liu'
    return '设置Session.'

@app.route('/get_session')
def get_session():
    username = session.get('username')
    if username is None:
        return 'Null'
    return username

@app.route('/del_session')
def del_session():
    session.pop('username')
    return "删除Session"

if __name__ == "__main__":
    app.run()