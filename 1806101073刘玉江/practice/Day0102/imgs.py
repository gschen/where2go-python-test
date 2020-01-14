from flask import Flask, Response, send_from_directory

app = Flask(__name__)

@app.route('/',methods = ['get'])
def index():
    def show_image():
        '''
        利用图片url用于显示
        '''
        with open('C:\\Users\\19145\\Desktop\\文件\\图片\\style\\IMG_0547.jpg', 'rb') as f:
            image = f.read()
        pic_url = Response(image, mimetype="image/jpeg")
        return pic_url




if __name__ == '__main__':
    app.run()