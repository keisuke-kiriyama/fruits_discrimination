# -*- coding: utf-8 -*-
import sys
import os
import csv
from random import shuffle

names = {
    "banana": 0,
    "corn": 1,
    "greengrape": 2,
    "lemon": 3,
    "peer": 4
}

exts = ['.JPG', '.JPEG', '.PNG', '.BMP', '.GIF']


def search_dir(imgdir):
    dir_members = []
    for dirpath, dirnames, _ in os.walk(imgdir):
        for dirname in dirnames:
            dir_member = os.path.join(dirpath, dirname)
            dir_members.append(dir_member)
    return dir_members


def create_csv(dir_members, basename, num_of_train_image):
    with open(basename + '_test.csv', 'w') as test_f:
        with open(basename + '_train.csv', 'w') as train_f:
            csv_test_writer = csv.writer(test_f)
            csv_train_writer = csv.writer(train_f)
            for dir_member in dir_members:
                file_list = os.listdir(dir_member)
                shuffle(file_list)
                category = dir_member.split('/')[-1]
                label = names[category]
                for n, img_name in enumerate(file_list):
                    (img, ext) = os.path.splitext(img_name)
                    img_path = os.path.join(dir_member, img_name)
                    if ext.upper() not in exts:
                        continue
                    if n < num_of_train_image:
                        csv_train_writer.writerow([img_path, label])
                    else:
                        csv_test_writer.writerow([img_path, label])


if __name__ == '__main__':
    imgdir = sys.argv[1]
    num_of_train_image = int(sys.argv[2])
    if not os.path.isdir(imgdir):
        sys.exit('%s is not directory' % imgdir)

    dir_members = search_dir(imgdir)
    create_csv(dir_members, 'fruits_image', num_of_train_image)
