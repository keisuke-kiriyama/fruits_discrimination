# -*- coding: utf-8 -*-

import cv2
import os
import sys
import random

def search_dir(imgdir):
    dir_members = []
    for dirpath, dirnames, _ in os.walk(imgdir):
        for dirname in dirnames:
            dir_member = os.path.join(dirpath, dirname)
            dir_members.append(dir_member)
    return dir_members


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
    img_x = random.randint(0, width - 56)
    img_y = random.randint(0, width - 56)
    img_width = 56
    img_height = 56

    tri_img = img[img_y:img_y+img_height, img_x:img_x+img_width]
    dst_path = os.path.join(triming_img_dir, file)
    cv2.imwrite(dst_path, tri_img)

if __name__ == '__main__':
    imgdir = sys.argv[1]
    triming_img_dir = sys.argv[2]
    num_of_trinming_img = int(sys.argv[3])
    if not os.path.isdir(imgdir):
        sys.exit('%s is not directory' % imgdir)
    dir_members = search_dir(imgdir)
    for dir_member in dir_members:
        dir_type = dir_member.split('/')[-1:]
        dst_path = os.path.join(triming_img_dir, dir_type[0])
        get_img(dir_member, num_of_trinming_img, dst_path)