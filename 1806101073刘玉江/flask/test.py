from flask import Flask, config, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config.from_object(config)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1914571065lyj@127.0.0.1:3306/java2019?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))


@app.route('/select')
def select_user():
    item = db.session.execute('select * from user order by id desc')
    item = list(item)
    return render_template('first.html', item=item)


@app.route('/add')
def add_user():
    user = User(id=1, username='liu', password='8989')
    db.session.add(user)
    return '添加成功'


@app.route('/delete')
def delete_user():
    User.query.filter_by(id=1).delete()
    return '删除成功'


@app.route('/update')
def update_user():
    User.query.filter_by(id=3).update({'password': 'nihao'})
    return '更改成功'


@app.route('/')
def index():
    return "你好"


if __name__ == '__main__':
    app.run(debug=True)
