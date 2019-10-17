from flask import Flask, url_for
from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel

app = Flask(__name__)
app.secret_key = 'super secret key'

babel = Babel(app)

# set optional bootswatch theme
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sctu123456@172.16.10.50/java2019'

db = SQLAlchemy(app, use_native_unicode='utf8')


admin = Admin(app, name='统一后台管理模板', template_mode='bootstrap3')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    score = db.Column(db.String(20))


db.create_all() # 第一次运行的时候所有的表。数据库需要自行创建。


class UserView(ModelView):
        can_delete = True  # disable model deletion

class CourseView(ModelView):
    pass

admin.add_view(UserView(User, db.session))
admin.add_view(CourseView(Course, db.session))


if __name__ == "__main__":
    
    app.run()

