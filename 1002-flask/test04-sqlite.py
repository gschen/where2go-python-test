from flask import Flask, url_for
from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'super secret key'


# set optional bootswatch theme

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' # 数据库文件绝对路径。
db = SQLAlchemy(app)


admin = Admin(app, name='统一后台管理模板', template_mode='bootstrap3')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# db.create_all() # create database and tables.

class UserView(ModelView):
        can_delete = False  # disable model deletion


admin.add_view(UserView(User, db.session))


if __name__ == "__main__":
    
    # app.config['SESSION_TYPE'] = 'filesystem'


    # app.debug = True
    app.run()

