# -*- coding: utf-8 -*-

import cv2
import os
import sys
import random

def get_img(imgdir, num_of_triming_img, triming_img_dir):
    files = os.listdir(imgdir)
    for i, file in enumerate(files):
        if(i == 0):continue
        file_path = os.path.join(imgdir, file)
        img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        for j in range(0, num_of_triming_img):
            file_num = (num_of_trinming_img * i) + j
            triming_img(img, triming_img_dir, str(file_num) + ".jpg")


def triming_img(img, triming_img_dir, file):
    if len(img.shape) == 3:
        height, width, channels = img.shape[:3]
    else:
        height, width = img.shape[:2]

    rand_x = random.randint(0, width/2)
    rand_y = random.randint(0, height/2)
    rand_width = random.randint(width/2, (width - rand_x))
    rand_height = random.randint(height/2, (height - rand_y))

    tri_img = img[rand_y:rand_y+rand_height, rand_x:rand_x+rand_width]
    dst_path = os.path.join(triming_img_dir, file)
    cv2.imwrite(dst_path, tri_img)

if __name__ == '__main__':
    imgdir = sys.argv[1]
    triming_img_dir = sys.argv[2]
    num_of_trinming_img = int(sys.argv[3])
    if not os.path.isdir(imgdir):
        sys.exit('%s is not directory' % imgdir)
    get_img(imgdir, num_of_trinming_img, triming_img_dir)
