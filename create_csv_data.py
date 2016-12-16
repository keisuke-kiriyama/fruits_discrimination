# -*- coding: utf-8 -*-
import sys
import os
import csv

names = {
        "banana_resize": 0,
        "corn_resize": 1,
        "greengrape_resize": 2,
        "lemon_resize": 3,
        "peer_resize": 4
    }

exts = ['.JPG', '.JPEG', '.PNG', '.BMP', '.GIF']



def dir_label(imgdir):
    for dirpath, dirnames, filenames in os.walk(imgdir):
        for dirname in dirnames:
            if dirname in names:
                n = names[dirname]
                member_dir = os.path.join(dirpath, dirname)
                create_csv(member_dir, n, dirname)

def create_csv(member_dir, n, dirname):
    for bottom_dirpath, bottom_dirnames, imgnames in os.walk(member_dir):
        if not bottom_dirpath.endswith(dirname):
            continue
        for imgname in imgnames:
            (img, ext) = os.path.splitext(imgname)
            if ext.upper() in exts:
                list_data = []
                img_path = os.path.join(bottom_dirpath, imgname)
                list_data.append(img_path)
                list_data.append(n)
                csv_writer.writerow(list_data)

if __name__ == '__main__':
    imgdir = sys.argv[1]
    if not os.path.isdir(imgdir):
        sys.exit('%s is not directory' % imgdir)

    with open('tes.csv', 'w') as f:
        csv_writer = csv.writer(f)
        dir_label(imgdir)



    f.close()





