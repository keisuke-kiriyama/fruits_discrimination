from flask import Flask, request, jsonify
import uuid
from werkzeug.utils import secure_filename
import sys
import os
import io
import numpy as np
from PIL import Image
import base64
import datetime
import time
from io import BytesIO


call_func_dir = os.path.dirname(os.path.abspath(__file__))
recog_img_dir = call_func_dir + '/../recognition_image'
log_dir = call_func_dir + '/../log_texture_gray'
ckpt_path = os.path.join(log_dir, 'model.ckpt-2000')
sys.path.append(recog_img_dir)
import prediction_fruits_discrimination

app = Flask(__name__)
app.debug = True

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "ok"})

@app.route('/upload', methods=['POST'])
def upload():
    #uploaded_image = request.files['file']
    print(request.content_length)
    uploaded_image = request.data
    #uploaded_image = request.form['file']
    print(len(uploaded_image))
    img = base64.b64decode(uploaded_image)
    #upload_image = request.data
    #img = Image.open(io.BytesIO(uploaded_image))
    #img = np.frombuffer(img)
    img = Image.open(io.BytesIO(img))
    img = np.array(img)
    print(img.shape)
    start = time.time()
    res = prediction_fruits_discrimination.execute(img, ckpt_path)
    elapsed_time = time.time() - start
    print(elapsed_time)
    #print(uploaded_image)
    return jsonify({'results':res})
    #return jsonify({'results': "uploaded_image"})

@app.route('/post', methods=['POST'])
def post_img():
    uploaded_image = request.files['file']
    img = Image.open(io.BytesIO(uploaded_image.read()))
    img = np.array(img)
    res = prediction_fruits_discrimination.execute(img, ckpt_path)
    return jsonify({'results':res})


@app.route('/show', methods=['GET'])
def show():
    # uploaded_image = request.files['file']
    # img = Image.open(io.BytesIO(uploaded_image.read()))
    # img.show()
    # return jsonify({'message':'ok'})
    uploaded_image = request.args.get('img')
    img = base64.standard_b64decode(uploaded_image)
    img = Image.open(io.BytesIO(img))
    img.show()
    return jsonify({'message': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# filename = secure_filename(f.filename)
    # (fn, ext) = os.path.splitext(filename)
    # input_path = '/tmp/' + uuid.uuid1().hex + ext
    # print(input_path)
    # f.save(input_path)
    # res = prediction_fruits_discrimination.execute(input_path, ckpt_path)
