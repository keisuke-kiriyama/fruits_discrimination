# -*- coding: utf-8 -*-

import cv2
import os

#file_dirにオリジナルディレクトリのpath指定
#resize_dirに出力先ディレクトリのpath指定

file_dir = '/Users/kiriyamakeisuke/practiceTensorFlow/fruits_discrimination/image_for_prediction'
files = os.listdir(file_dir)
for i, file in enumerate(files):
    #if file.split('.')[0].split('_')[-1] == '0':
    if i > 0:
        file_path = file_dir + '/' + file
        print(file_path)

        img = cv2.imread(file_path, cv2.IMREAD_COLOR)

        size = (56, 56)
        resize_img = cv2.resize(img, size)
        os.remove(file_path)
        cv2.imwrite(file_path, resize_img)
