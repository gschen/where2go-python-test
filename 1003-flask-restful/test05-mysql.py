from flask import Flask
from flask_restalchemy import Api

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

app = Flask("tour-of-heroes")


@app.route("/create_db", methods=["POST"])
def create_db():
    db.create_all()
    return "DB created"


# Set an SQLite in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sctu123456@172.16.10.50/java2019'
db.init_app(app)  # Must be called before Api object creation

api = Api(app)
api.add_model(User, "/users")

if __name__ == "__main__":
    app.run()
