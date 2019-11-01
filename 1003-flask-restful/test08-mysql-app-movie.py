# -*- coding: UTF-8 -*-

from flask import Flask
from flask_restalchemy import Api

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView

import requests
from bs4 import BeautifulSoup

db = SQLAlchemy()

#########################################################################################################
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(200))
    movie_href = db.Column(db.String(200))

class MovieView(ModelView):
    can_delete = True  # disable model deletion
#########################################################################################################

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

@app.route('/add', methods=['GET'])
def add_data():
    soup = BeautifulSoup(requests.get('https://www.kankanwu.com/Animation/').content)
    for a in soup.select('dd > a'):
        try:
            db.session.add(Movie(movie_title=a['title'], movie_href=a['href']))
            db.session.commit()
        except Exception as e:
            print(e)

# RestAPI 配置部分
api = Api(app)
api.add_model(Movie, "/movies")



# 后台管理页面
admin = Admin(app, name='统一后台管理模板', template_mode='bootstrap3')
admin.add_view(MovieView(Movie, db.session))

if __name__ == "__main__":
    app.run()
