#! -*- coding: utf-8 -*-

import sys
import numpy as np
import tensorflow as tf
import os
import input_image_data
import model_fruits_discrimination

def evaluation(img, ckpt_path):
    tf.reset_default_graph()

    #img = np.array(img)

    #jpeg = tf.read_file(img)
    #img = tf.image.decode_jpeg(img, channels=3)
    img = tf.cast(img, tf.float32)
    img.set_shape([input_image_data.IMAGE_SIZE, input_image_data.IMAGE_SIZE, 3])
    #img = tf.image.resize_images(img, input_image_data.DST_INPUT_SIZE, input_image_data.DST_INPUT_SIZE)
    img = tf.image.per_image_whitening(img)
    img = tf.reshape(img, [-1, input_image_data.DST_INPUT_SIZE * input_image_data.DST_INPUT_SIZE * 3])

    #logits = model_fruits_discrimination.inference(img, 1.0, input_image_data.DST_INPUT_SIZE, input_image_data.NUM_CLASS)
    logits = model_fruits_discrimination.deep_inference(img, 1.0, input_image_data.DST_INPUT_SIZE,
                                                   input_image_data.NUM_CLASS)
    sess = tf.InteractiveSession()
    saver = tf.train.Saver()
    sess.run(tf.initialize_all_variables())
    if ckpt_path:
        saver.restore(sess, ckpt_path)

    softmax = logits.eval()

    result = softmax[0]
    rates = [round(n * 100.0, 1) for n in result]
    #print(img_path)
    print(rates)

    pred = np.argmax(result)
    print(input_image_data.FOOD_NAMES[pred])

    foods = []
    for i, rate in enumerate(rates):
        name = input_image_data.FOOD_NAMES[i]
        foods.append({
            'name_ascii': name[1],
            'name': name[0],
            'rate': rate
        })
    rank = sorted(foods, key=lambda x: x['rate'], reverse=True)

    #return (rank, pred)
    return input_image_data.FOOD_NAMES[pred]

# def execute(imgdir_path, ckpt_path):
#     res = []
#     file_list = os.listdir(imgdir_path)
#     for img_path in file_list:
#         (rank, pred) = evaluation(img_path, ckpt_path)
#         res.append({
#             'file': img_path,
#             'top_member_id': pred,
#             'rank': rank
#         })
#     return res

def execute(img, ckpt_path):
    res = evaluation(img, ckpt_path)
    # (rank, pred) = evaluation(img_path, ckpt_path)
    # res.append({
    #     'file': img_path,
    #     'top_member_id': pred,
    #     'rank': rank
    # })

    return res

# def search_img(imgdir_path, ckpt_path):
#     file_list = os.listdir(imgdir_path)
#     for img_name in file_list:
#         if not img_name.endswith('.jpg'):
#             continue
#         img_path = os.path.join(imgdir_path, img_name)
#         execute(img_path, ckpt_path)


# if __name__ == '__main__':
#     recognition_dir = os.path.dirname(os.path.abspath(__file__))
#     log_dir = recognition_dir + '/../log'
#     ckpt_path = os.path.join(log_dir, 'model.ckpt-4999')
#     print(ckpt_path)
#     imgdir_path = sys.argv[1]
#     search_img(imgdir_path, ckpt_path)
    #print(execute(img_path, ckpt_path))
    #execute(img_path, ckpt_path)