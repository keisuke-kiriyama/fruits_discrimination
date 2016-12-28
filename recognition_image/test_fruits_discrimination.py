# -*- coding: utf-8 -*-
import sys
import numpy as np
import tensorflow as tf

import input_image_data
import model_fruits_discrimination

def main(ckpt_path, csv = 'fruits_image_test.txt'):
    with tf.Graph().as_default():
        images, labels, filename = input_image_data.load_data_for_test([csv], 610)
        #print 'start', images, labels
        keep_prob = tf.placeholder("float")

        #logits = model_fruits_discrimination.inference(images, keep_prob, input_image_data.DST_INPUT_SIZE, input_image_data.NUM_CLASS)
        logits = model_fruits_discrimination.deep_inference(images, keep_prob, input_image_data.DST_INPUT_SIZE, input_image_data.NUM_CLASS)
        acc = model_fruits_discrimination.accuracy(logits, labels)

        saver = tf.train.Saver()
        sess = tf.Session()
        sess.run(tf.initialize_all_variables())
        saver.restore(sess, ckpt_path)
        tf.train.start_queue_runners(sess)

        acc_res, filename_res, actual_res, expect_res = sess.run([acc, filename, logits, labels], feed_dict={keep_prob: 1.0})
        print('accuracy', acc_res)
        #return

        goods = []
        bads = []
        for idx, (act, exp) in enumerate(zip(actual_res, expect_res)):
            if np.argmax(act) == np.argmax(exp):
                goods.append(filename_res[idx])
            else:
                bads.append(filename_res[idx])
        print('good')
        for f in goods:
            print('cp',f,'out_goods')
        print('bad')
        for f in bads:
            print('cp',f,'out_bads')
        #correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))


if __name__ == '__main__':
    ckpt_path = sys.argv[1]
    csv = sys.argv[2]
    #print ckpt_path
    main(ckpt_path, csv)