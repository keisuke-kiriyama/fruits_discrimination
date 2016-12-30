from flask import Flask, request, jsonify
import uuid
from werkzeug.utils import secure_filename
import sys
import os
import io
import numpy as np
from PIL import Image
from io import BytesIO

call_func_dir = os.path.dirname(os.path.abspath(__file__))
recog_img_dir = call_func_dir + '/../recognition_image'
log_dir = call_func_dir + '/../log'
ckpt_path = os.path.join(log_dir, 'model.ckpt-3000')
sys.path.append(recog_img_dir)
import prediction_fruits_discrimination

app = Flask(__name__)
app.debug = True


@app.route('/upload', methods=['POST'])
def upload():
    uploaded_image = request.files['file']
    img = Image.open(io.BytesIO(uploaded_image.read()))
    img = np.array(img)
    res = prediction_fruits_discrimination.execute(img, ckpt_path)
    return jsonify({'results':res})

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# filename = secure_filename(f.filename)
    # (fn, ext) = os.path.splitext(filename)
    # input_path = '/tmp/' + uuid.uuid1().hex + ext
    # print(input_path)
    # f.save(input_path)
    # res = prediction_fruits_discrimination.execute(input_path, ckpt_path)
