import json

from flask import Flask, request, render_template, redirect, url_for, flash, session
import requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
    get_data = request.args.to_dict()
    content = get_data.get('content')
    content = str(content)
    url = url + content
    res = requests.get(url)
    data = res.json()
    data_content = data['content']
    return render_template("index.html", data_content=data_content)





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
