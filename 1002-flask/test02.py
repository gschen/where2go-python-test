from flask import Flask
from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView





app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')

# Add administrative views here
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')
    
admin.add_view(MyView(name='Hello'))


app.run()


