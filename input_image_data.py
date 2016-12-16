# -*- coding: utf-8 -*-
import sys
import cv2
import random
import numpy as np
import os
import tensorflow as tf

NUM_CLASS = 5
IMAGE_SIZE = 112

FOOD_NAMES = {
    0: 'banana',
    1: 'corn',
    2: 'greengrape',
    3: 'lemon',
    4: 'peer'
}

EXTS = ['.JPG', '.JPEG', '.PNG', '.BMP']

def load_data(csv, batch_size, shuffle = True, distored = True):
    queue = tf.train.string_input_producer(csv, shuffle=shuffle)
    reader = tf.TextLineReader()
    key, value = reader.read(queue)
    filename, label = tf.decode_csv(value, [["path"], [1]], field_delim = " ")
    label = tf.cast(label, tf.int64)
    label = tf.one_hot(label, depth = NUM_CLASS, on_value = 1.0, off_value = 0.0, axis = -1)

    (imgpath, ext) = os.path.splitext(filename)
    n = EXTS.index(ext)

    if n == 0 or n == 1:
        jpeg = tf.read_file(filename)
        image = tf.image.decode_jpeg(jpeg, channels=3)
        image = tf.cast(image, tf.float32)
        image.set_shape([IMAGE_SIZE, IMAGE_SIZE, 3])
    elif n == 2:
        png = tf.read_file(filename)
        image = tf.image.decode_png(png, channels=3)
        image = tf.cast(image, tf.float32)
        image.set_shape([IMAGE_SIZE, IMAGE_SIZE, 3])
    elif n == 3:
        pass



