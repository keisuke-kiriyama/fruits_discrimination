# -*- coding:utf-8 -*-
import sys
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.python.pywrap_tensorflow
from datetime import datetime
import random
import time
import os

import input_image_data
import model_fruits_discrimination

LOGDIR = '/Users/kiriyamakeisuke/practiceTensorFlow/fruits_discrimination/log_texture'
print(LOGDIR)

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('train', 'texture_image_train.txt', 'File name of train data')
flags.DEFINE_string('test', 'texture_image_test.txt', 'File name of test data')
flags.DEFINE_string('train_dir', LOGDIR, 'Directory to put the training data.')
flags.DEFINE_integer('max_steps', 1001, 'Number of steps to run trainer.')
flags.DEFINE_integer('batch_size', 200, 'Batch size Must divide evenly into the dataset sizes.')
flags.DEFINE_float('learning_rate', 1e-4, 'Initial learning rate.')


def main(ckpt = None):
    with tf.Graph().as_default():
        keep_prob = tf.placeholder("float")

        images, labels, _ = input_image_data.load_data([FLAGS.train], FLAGS.batch_size, shuffle = True, distored = True)
        #logits = model_fruits_discrimination.texture_inference(images, keep_prob, input_image_data.DST_INPUT_SIZE, input_image_data.NUM_CLASS)
        logits = model_fruits_discrimination.inference(images, keep_prob, input_image_data.DST_INPUT_SIZE, input_image_data.NUM_CLASS)
        #logits = model_fruits_discrimination.deep_inference(images, keep_prob, input_image_data.DST_INPUT_SIZE, input_image_data.NUM_CLASS)
        loss_value = model_fruits_discrimination.loss(logits, labels)
        train_op = model_fruits_discrimination.training(loss_value, FLAGS.learning_rate)
        acc = model_fruits_discrimination.accuracy(logits, labels)

        saver = tf.train.Saver(max_to_keep = 0)
        sess = tf.Session()
        sess.run(tf.initialize_all_variables())
        if ckpt:
            print('restore ckpt', ckpt)
            saver.restore(sess, ckpt)
        tf.train.start_queue_runners(sess)
        summary_op = tf.merge_all_summaries()
        summary_writer = tf.train.SummaryWriter(FLAGS.train_dir, sess.graph_def)

        for step in range(FLAGS.max_steps):
            start_time = time.time()
            _, loss_res, acc_ress = sess.run([train_op, loss_value, acc], feed_dict={keep_prob: 0.5})
            duration = time.time() - start_time

            if step % 10 == 0:
                num_examples_per_step = FLAGS.batch_size
                example_per_sec = num_examples_per_step / duration
                sec_per_batch = float(duration)
                format_str = ('%s: step %d, loss = %.2f (%.1f examples/sec; %.3f sec/batch)')
                print(format_str % (datetime.now(), step, loss_res, example_per_sec, sec_per_batch))
                print('accuracy', acc_ress * 100, '%')

            if step % 100 == 0:
                summary_str = sess.run(summary_op, feed_dict={keep_prob: 1.0})
                summary_writer.add_summary(summary_str, step)

            if step % 1000 == 0 or (step + 1) == FLAGS.max_steps or loss_res == 0:
                checkpoint_path = os.path.join(FLAGS.train_dir, 'model.ckpt')
                saver.save(sess, checkpoint_path, global_step=step)

            # if loss_res == 0:
            #     print('loss is zero')
            #     break

if __name__ == '__main__':
    ckpt = None
    if len(sys.argv) == 2:
        ckpt = sys.argv[1]
    main(ckpt)
