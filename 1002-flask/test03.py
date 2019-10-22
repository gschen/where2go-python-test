from flask import Flask, url_for
from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='统一后台管理模板', template_mode='bootstrap3')

# Add administrative views here
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('hello.html')
    
class TestView(BaseView):
    @expose('/')
    def index(self):
        return self.render('test.html')

admin.add_view(MyView(name='Hello'))
admin.add_view(TestView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(TestView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(TestView(name='Hello 3', endpoint='test3', category='Test'))

app.run()


