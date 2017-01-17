# -*- coding: utf-8 -*-

import cv2
import os
import sys

#file_dirにオリジナルディレクトリのpath指定
#resize_dirに出力先ディレクトリのpath指定

def search_dir(imgdir):
    dir_members = []
    for dirpath, dirnames, _ in os.walk(imgdir):
        for dirname in dirnames:
            dir_member = os.path.join(dirpath, dirname)
            dir_members.append(dir_member)
    return dir_members

def resize_img(dirmembers):
    for dirmember in dirmembers:
        files = os.listdir(dirmember)
        for i, file in enumerate(files):
            if i > 0:
                file_path = dirmember + '/' + file
                print(file_path)
                img = cv2.imread(file_path, cv2.IMREAD_COLOR)
                size = (56, 56)
                resize_img = cv2.resize(img, size)
                os.remove(file_path)
                cv2.imwrite(file_path, resize_img)


if __name__ == '__main__':
    file_dir = sys.argv[1]
    if not os.path.isdir(file_dir):
        sys.exit('%s is not directory' % file_dir)

    dir_members = search_dir(file_dir)
    resize_img(dir_members)