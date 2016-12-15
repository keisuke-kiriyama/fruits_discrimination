# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os

#file_dirにオリジナルディレクトリのpath指定
#resize_dirに出力先ディレクトリのpath指定

file_dir = '/Users/kiriyamakeisuke/practiceTensorFlow/fruits_discrimination/images/test/lemon'
resize_dir = '/Users/kiriyamakeisuke/practiceTensorFlow/fruits_discrimination/images/test_resize/lemon_resize'
files = os.listdir(file_dir)
for i, file in enumerate(files):
    if i > 0:
        file_path = file_dir + '/' + file
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)

        size = (28, 28)
        resize_img = cv2.resize(img, size)

        cv2.imwrite(resize_dir + '/' + file, resize_img)
