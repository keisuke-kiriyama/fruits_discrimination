# -*- coding: utf-8 -*-

import cv2
import os
import sys

def search_dir(imgdir):
    dir_members = []
    for dirpath, dirnames, _ in os.walk(imgdir):
        for dirname in dirnames:
            dir_member = os.path.join(dirpath, dirname)
            dir_members.append(dir_member)
    return dir_members

def convert_gray_img(dir_members):
    for dirmember in dir_members:
        files = os.listdir(dirmember)
        for i, file in enumerate(files):
            if i > 0:
                file_path = dirmember + '/' + file
                print(file_path)
                img = cv2.imread(file_path, cv2.IMREAD_COLOR)
                gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                img = cv2.merge((gray, gray, gray))
                cv2.imwrite(file_path, imgc)

if __name__ == '__main__':
    file_dir = sys.argv[1]
    if not os.path.isdir(file_dir):
        sys.exit('%s is not directory' % file_dir)

    dir_members = search_dir(file_dir)
    convert_gray_img(dir_members)