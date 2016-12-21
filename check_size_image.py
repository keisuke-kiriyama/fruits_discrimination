# -*- coding: utf-8 -*-
import sys
import os
import cv2


def search_dir(imgdir):
    dir_members = []
    for dirpath, dirnames, _ in os.walk(imgdir):
        for dirname in dirnames:
            dir_member = os.path.join(dirpath, dirname)
            dir_members.append(dir_member)
    return dir_members



if __name__ == '__main__' :

    img_dir = sys.argv[1]

    dirmembers = search_dir(img_dir)
    for dirmember in dirmembers:
        file_images = os.listdir(dirmember)
        for image_name in file_images:
            if not image_name.endswith('.jpg'):
                continue
            image_path = os.path.join(dirmember, image_name)
            image = cv2.imread(image_path)
            if not image.shape[0] == 56:
                print(image_path)
            if not image.shape[1] == 56:
                print(image_path)
