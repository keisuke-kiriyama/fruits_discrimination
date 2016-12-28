# -*- coding:utf-8 -*-

import os
import sys
import cv2

names = {
    "banana": 0,
    "corn": 1,
    "greengrape": 2,
    "lemon": 3,
    "peer": 4
}

def search_dir(imgdir):
    dir_members = []
    for dirpath, dirnames, _ in os.walk(imgdir):
        for dirname in dirnames:
            dir_member = os.path.join(dirpath, dirname)
            dir_members.append(dir_member)
    return dir_members

def search_png_img(dir_members):
    for dir_member in dir_members:
        file_list = os.listdir(dir_member)
        for n, img_name in enumerate(file_list):
            (img, ext) = os.path.splitext(img_name)
            img_path = os.path.join(dir_member, img_name)
            if ext.upper() == '.PNG':
                convert_png2jpg(img_path)
                os.remove(img_path)

def convert_png2jpg(img_path):
    png_img = cv2.imread(img_path)
    img_remove_ext = img_path.split('.')[:-1]
    jpg_path = img_remove_ext[0] + '.jpg'
    cv2.imwrite(jpg_path, png_img)


if __name__ == '__main__':
    imgdir = sys.argv[1]
    if not os.path.isdir(imgdir):
        sys.exit('%s is not directory' % imgdir)

    dir_members = search_dir(imgdir)
    search_png_img(dir_members)