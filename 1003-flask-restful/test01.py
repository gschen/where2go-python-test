from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Test(Resource):

    def get(self):
        return {'name':'chen'}


api.add_resource(HelloWorld, '/')
api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run()
