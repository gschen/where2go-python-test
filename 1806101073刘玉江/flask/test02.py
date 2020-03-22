from flask import Flask, app, config, render_template, jsonify

from flask import Response, json
app = Flask(__name__)


@app.route('/')
def test():
    return render_template('test02.html')


@app.route('/json1')
def jason1():
    s = ['张三', '年龄', '姓名']
    t = {}
    t['data'] = s
    print(t)
    return json.dumps(t, ensure_ascii=False)

@app.route('/json2')
def jason2():
    s = ['张三', '年龄', '姓名']
    print(s)
    return json.dumps(s, ensure_ascii=False)

#使用json转换的在前端显示的数据为JSON字符串。


#使用flask的jsonify转换后，在前台显示的为JSON对象：
@app.route('/json3')
def jason3():
    s = ['zhangsan', 'age', 'name']
    return jsonify(s)

#返回多条数据
@app.route('/json4')
def jason4():
    s = ['zhangsan', 'age', 'name']
    t={}
    for i in range(1,5):
        t[str(i)] = s
    return json.dumps(t,ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)
