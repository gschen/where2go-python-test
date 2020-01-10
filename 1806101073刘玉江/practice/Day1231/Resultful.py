from flask import Flask, render_template, url_for
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class IndexView(Resource):
    def get(self):  # GET
        return {"username": "liu"}

    def post(self):  # POST
        return {"password": "123"}


api.add_resource(IndexView, '/test/', endpoint='index', )


# 带参数操作
class IndexView1(Resource):
    def get(self, id):  # get
        str = '(get)id = %d' % id
        return {'msg': str}

    def post(self, id):  # post
        str = '(post)id = %d' % id
        return {'msg': str}


api.add_resource(IndexView1, '/test1/<int:id>', endpoint='test1')


# 多个url访问
class IndexView2(Resource):
    def get(self):
        return {"msg": "hello"}


api.add_resource(IndexView2, '/test2', '/test3', '/test4', endpoint='test2')

if __name__ == '__main__':
    app.run(debug=True)
