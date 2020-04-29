from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test07.html')


@app.route('/setcookie',methods = ['post','get'])
def setcookie():
    if request.method=="POST":
        user = request.form['nm']
        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie('userid',user)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userid')
    if name is None:
        return "Null"
    return name

if __name__ == "__main__":
    app.run()
