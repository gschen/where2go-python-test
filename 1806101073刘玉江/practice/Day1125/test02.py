from flask import Flask, config
import json
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1914571065lyj@127.0.0.1:3306/python2019?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'student'
    sno = db.Column(db.String, primary_key=True)
    sname = db.Column(db.String)
    ssex = db.Column(db.String)


@app.route('/test')
def test():
    item = User.query.filter_by(sno='1').first()
    print(item)
    print(type(item))
    print(item.sno)
    dict1 = {}
    dict1['sno'] = item.sno
    dict1['sname'] = item.sname
    dict1['ssex'] = item.ssex
    print(dict1)
    print(type(dict1))
    dict1 = json.dumps(dict1, ensure_ascii=False) #字典转json字符串
    print(type(dict1))
    dict1 = json.loads(dict1) #json字符串转字典
    print(type(dict1))
    return dict1


@app.route('/')
def index():
    # item = db.session.execute('select * from student')
    item = User.query.all()
    print(item)
    print(len(item))
    result = []
    # [{"sno":"1"，"sname":"liu","ssex":"男"}，{"sno":"1","sname":"zhang","ssex":"女"}]
    for i in item:
        dict1 = {}
        dict1['sno'] = i.sno
        dict1['sname'] = i.sname
        dict1['ssex'] = i.ssex
        # print(dict1)
        result.append(dict1)
        # print(result)
    print(result)
    print(type(result))
    print(result[0]['sno'])
    result = json.dumps(result, ensure_ascii=False)
    print(type(result))
    print(result[0])
    return result


if __name__ == "__main__":
    app.run(debug=True)
