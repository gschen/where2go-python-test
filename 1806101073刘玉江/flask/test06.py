import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    data = request.form['data']  # 获取值
    return json.dumps(data, ensure_ascii=False)


@app.route('/add1', methods=['post'])
def Add1():
    # raw
    get_data = request.get_data()
    # 将bytes类型转换为json数据
    get_data = json.loads(get_data)
    num1 = get_data.get('num1')
    num2 = get_data.get('num2')
    return json.dumps(int(num1) + int(num2), ensure_ascii=False)


@app.route('/add2', methods=['GET'])
def Add2():
    get_data = request.args.to_dict()  # 获取传入的params参数
    num1 = get_data.get('num1')
    num2 = get_data.get('num2')
    return json.dumps(int(num2) + int(num1), ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
