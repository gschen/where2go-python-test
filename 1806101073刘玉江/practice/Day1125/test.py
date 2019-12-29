from flask import Flask, config, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1914571065lyj@127.0.0.1:3306/java2019?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 't_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))


@app.route('/')
def select_user():
    item = db.session.execute('select * from t_users order by id desc')
    item = list(item)
    print(item)
    for i in range(len(item)):
        item[i] = list(item[i])
    print(item)
    keys = ['学号', '姓名', '性别']
    print(keys)
    result = []
    for i in range(len(item)):
        list_json = dict(zip(keys, item[i]))
        print(item[i])
        result.append(list_json)
    print(result)
    print(type(result))
    str_json = json.dumps(result, ensure_ascii=False)  # json转为string
    a = json.loads(str_json)
    print(a)
    print(type(a))
    print(str_json)
    print(type(str_json))
    return str_json


if __name__ == "__main__":
    app.run(debug=True)
