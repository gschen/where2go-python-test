from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/')
def index():
    resp = Response("设置Cookie")
    resp.set_cookie('username', 'liu',)
    return resp

@app.route('/del')
def delete():
    resp = Response("删除Cookie")
    resp.delete_cookie('username')
    return resp


if __name__ == "__main__":
    app.run()
