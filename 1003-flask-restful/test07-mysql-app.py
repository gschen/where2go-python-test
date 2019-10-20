# -*- coding: UTF-8 -*-

from flask import Flask
from flask_restalchemy import Api

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class UserView(ModelView):
        can_delete = True  # disable model deletion


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(100))

class JobView(ModelView):
    pass


app = Flask("tour-of-heroes")
app.secret_key = 'super secret key'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sctu123!@#@47.104.80.155/javaweb'
db.init_app(app)  # Must be called before Api object creation

# 第一次运行需要执行这个 localhost:5000/create_db 创建所有的表
@app.route("/create_db", methods=["GET"])
def create_db():
    db.create_all()
    return "DB created"

# RestAPI 配置部分
api = Api(app)
api.add_model(User, "/users")
api.add_model(Job, "/jobs")


# 后台管理部分
admin = Admin(app, name='统一后台管理模板', template_mode='bootstrap3')
admin.add_view(UserView(User, db.session))
admin.add_view(JobView(Job, db.session))

if __name__ == "__main__":
    app.run()
