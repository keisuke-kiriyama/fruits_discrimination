from flask import Flask, Response, request, jsonify
import uuid
from werkzeug.utils import secure_filename
import sys
import os

call_func_dir = os.path.dirname(os.path.abspath(__file__))
recog_img_dir = call_func_dir + '/../recognition_image'
log_dir = call_func_dir + '/../log'
ckpt_path = os.path.join(log_dir, 'model.ckpt-4999')
sys.path.append(recog_img_dir)
import prediction_fruits_discrimination

app = Flask(__name__)
app.debug = True

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    filename = secure_filename(f.filename)
    (fn, ext) = os.path.splitext(filename)
    input_path = '/tmp/' + uuid.uuid1().hex + ext
    print(input_path)
    f.save(input_path)
    res = prediction_fruits_discrimination.execute(input_path, ckpt_path)
    return jsonify({'results':res})

if __name__ == '__main__':
    app.run(host='0.0.0.0')


