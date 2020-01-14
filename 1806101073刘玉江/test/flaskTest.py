import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def index():
    # raw
    get_data = request.get_data()
    # 将bytes类型转换为json数据（）
    get_data = str(get_data, 'utf-8')
    get_data = json.loads(get_data)
    num1 = get_data.get('num1')
    num2 = get_data.get('num2')
    # num1和num2都是字符串类型
    # 得到的是两个字符串相连
    return json.dumps(int(num1) + int(num2), ensure_ascii=False)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
