#coding=utf-8

import os
import glob

from PIL import Image


files=glob.glob(u"\\20190820\\*\\*\\*.jpg")


print len(files)
print  files
# for f in files:
#     os.rename(f,f.split('.')[0]+".png")

# for f in files:
#     os.remove(f)


def rename_to_png(files):
    for f in files:
        os.rename(f,f.split('.')[0]+".png")

rename_to_png(files)

def png_to_jpg(files):
    for filename in files:
        path = ''
        path = filename
        img=Image.open(path)
        if img.mode == "P":
            img = img.convert('RGB')
        if img.mode == "RGBA":
            img = img.convert('RGB')
        img.save(path.split('.')[0] + ".jpg")
        print "%s has been changed!" % filename
        # os.remove(path)

# png_to_jpg(files)
