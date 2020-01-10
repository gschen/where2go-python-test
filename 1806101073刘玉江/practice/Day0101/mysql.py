from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, fields, marshal_with, Api

app = Flask(__name__)
api = Api(app)
app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myroot:myroot@47.95.235.93:3306/java2019?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SECRET_KEY"] = '235c749859ec44c2bd6064ec6da7b927'
db = SQLAlchemy(app)


class T_users(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


class T_USERS(Resource):
    user = {
        'id': fields.String(),
        'username': fields.String(),
        'password': fields.String()
    }

    @marshal_with(user)
    def get(self):
        user = T_users.query.all()
        return user


api.add_resource(T_USERS, '/', endpoint='test')


@app.route('/')
def index():
    admin = T_users.query.all()
    a = admin.id
    return a


if __name__ == '__main__':
    app.run()
