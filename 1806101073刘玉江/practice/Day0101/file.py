import hashlib
import json
import os
import random
import time

import requests
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "upload/")


def creat_folder(folder_path):
 if not os.path.exists(folder_path):
     os.mkdir(folder_path)
     os.chmod(folder_path,os.O_RDWR)

def md5(data):
 	md = hashlib.md5()
 	md.update(data.encode('utf-8'))
 	data = md.hexdigest()
 	return data

@app.route('/api/v/upload/<name>',methods=['POST','GET'])
def mp_img(openid):
    fn = time.strftime('%Y%m%d%H%M%S') + '_%d' % random.randint(0, 100) + '.png'
    avata = request.files.get('test')
    hash_openid = md5(openid)
    new = compression_img(avata)
    creat_folder(os.path.join(app.config['UPLOADS_FOLDER'], hash_openid))
    pic_dir = os.path.join(app.config['UPLOADS_FOLDER'], hash_openid, fn)
    new.save(pic_dir)
    folder = photosSet.url(hash_openid)
    img_dir= folder + '/' + fn
    return img_dir


@app.route('/api/v/userinfo',methods=['POST'])
def userinfo():
    info = request.values.get('info')
    appid = 'wx000000000032332'  #这里填你的appid
    secret = 'jd82hhewh808b3sddada915e0b3' #你的secret_key
    user_info = json.loads(info)
    code = user_info['code']
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
    appid, secret, code)
    data = requests.get(url).text
    session_ = json.loads(data)
    session_key = session_['session_key']
    encryptedData = user_info['encryptedData']
    iv = user_info['iv']
    pc = WXBizDataCrypt(appid, session_key)
    return pc.decrypt(encryptedData, iv)






if __name__ == '__main__':
    app.run(debug=True)
