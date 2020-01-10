import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods = ['post'])
def index():
    img = request.files.get('photo')
    username = request.form.get("name")
    path = basedir + "/uploads/"
    file_path = path + img.filename +'by'+username
    img.save(file_path)
    a = '上传头像成功，上传的用户是：'
    b = a + username
    return b



if __name__ == '__main__':
    app.run(debug=True)