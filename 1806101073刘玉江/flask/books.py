from flask import Flask, config, render_template, request, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import redirect

app = Flask(__name__)

app.config.from_object(config)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1914571065lyj@127.0.0.1:3306/java2019?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SECRET_KEY"] = '235c749859ec44c2bd6064ec6da7b927'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='书籍ID')
    name = db.Column(db.String(200), unique=True, comment='书籍名称')
    price = db.Column(db.DECIMAL, comment='书籍价格')


@app.route('/')
def index():
    books = Books.query.order_by(Books.id.desc()).all()
    return render_template('books.html', books=books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        new_name = Books(name=name, price=price)
        try:
            db.session.add(new_name)
            db.session.commit()
            flash('添加书籍成功!')
        except Exception:
            flash('添加失败（书籍名称重名或其他）')

    return render_template('add_books.html')


@app.route('/alter_book', methods=['GET', 'POST'])
def alter_book():
    book_id = request.args.get('book_id')
    one_book = Books.query.get(book_id)
    if request.method == 'POST':
        new_book = request.form.get('name')
        one_book.name = new_book
        db.session.add(one_book)
        db.session.commit()

        return redirect(url_for('alter_book'))
    return render_template('alter_books.html', one_book=one_book)

@app.route('/delete_book/<int:id>')
def delete_book(id=None):
    one_book =Books.query.filter_by(id=id).first_or_404()
    db.session.delete(one_book)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/buy_book')
def buy_book():
    if session.get('user_id'):
        return '可以购买'
    else:
        return '需要登录'


if __name__ == '__main__':
    app.run(debug=True)
