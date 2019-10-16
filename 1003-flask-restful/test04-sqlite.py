from flask import Flask
from flask_restalchemy import Api

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer


db = SQLAlchemy()


class Hero(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    secret_name = Column(String)


app = Flask("tour-of-heroes")


@app.route("/create_db", methods=["POST"])
def create_db():
    db.create_all()
    return "DB created"


# Set an SQLite in-memory database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db.init_app(app)  # Must be called before Api object creation

api = Api(app)
api.add_model(Hero, "/heroes")

if __name__ == "__main__":
    app.run()
