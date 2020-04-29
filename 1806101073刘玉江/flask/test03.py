import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        #raw
        a = request.get_data()
        #a类型为bytes
        print(a)
        dict1 = json.loads(a)
        #转换数据类型
        print(dict1)
        print(type(dict1))
        dict2 = json.dumps(dict1,ensure_ascii=False)
        print(dict2)
        print(type(dict2))
        return json.dumps(dict1)
    else:
        return '<h1>只接受post请求！</h1>'



# 只接受get方法访问
@app.route("/test", methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    #raw
    get_data1 = request.get_data()
    #获取到的值为bytes类型
    print(type(get_data1))
    print(get_data1)
    get_data1 = json.loads(get_data1)
    #转换为json数据
    print(type(get_data1))
    print(get_data1)
    name1 = get_data.get('name')

    age1 = get_data.get('age')

    # 调用tt函数对参数进行操作
    return_dict['result'] = tt(name1, age1)

    return json.dumps(return_dict, ensure_ascii=False)


@app.route('/add1', methods=['post'])
def Add1():
    #raw
    get_datax = request.get_data()
    print(get_datax)
    #将bytes类型转换为json数据
    get_datax = json.loads(get_datax)
    print(get_datax)
    num1 = get_datax.get('num1')
    num2 = get_datax.get('num2')
    #num1和num2都是字符串类型
    #得到的是两个字符串相连
    return json.dumps(num1 + num2, ensure_ascii=False)


@app.route('/add2', methods=['GET'])
def Add2():
    get_data = request.args.to_dict()
    num1 = get_data.get('num1')
    num2 = get_data.get('num2')
    return json.dumps(int(num2) + int(num1), ensure_ascii=False)


# 只接受post请求
@app.route('/test1', methods=["POST"])
def test1():
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    if request.get_data() is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取参数
    get_Data = request.get_data()
    print(get_Data)
    # 传入的参数为bytes类型，需要转化为jason
    get_Data = json.loads(get_Data)
    name = get_Data.get('name')
    age = get_Data.get('age')

    return_dict['result'] = tt(name, age)
    return json.dumps(return_dict, ensure_ascii=False)


@app.route('/test2')
def test2():
    #获取表单里的data
    data = request.form['data']
    print(type(data))

    return json.dumps(data,ensure_ascii=False)

def tt(name, age):
    result_str = "%s今年%s岁" % (name, age)
    return result_str


@app.route('/user/<name>')
def index2(name):
    return '<h1>hello,%s</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
