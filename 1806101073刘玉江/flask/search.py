from flask import Flask, config, render_template, request, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1914571065lyj@127.0.0.1:3306/java2019?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='ID')
    name = db.Column(db.String(255), unique=True, comment='名称')
    content = db.Column(db.String(255), comment='内容')


@app.route('/', methods=['post', 'get'])
def search():
    content = request.form.get('content')
    if content is None:
        content = " "
    quotes = Quotes.query.filter(Quotes.content.like("%"+content+"%")if content is not None else "").all()
    return render_template('search.html',quotes = quotes)


if __name__ == "__main__":
    app.run(debug=True)
