#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------------------
# grid_images
# 
#
# run on windows
#------------------------------------------
import os, sys
import cv2
import numpy as np
import numpy as np
from PIL import Image, ImageDraw

black = (0, 0, 0)
white = (255, 255, 255)

#dpath = "textile_seg_dataset"
train_percentage = 0.7
val_percentage = 0.3

if len(sys.argv) != 3:
    print('usage: python grid_images.py data_path desc_path')
    sys.exit(-1)

if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'

dpath = sys.argv[1].rstrip(path_linkage)
dpath2 = sys.argv[2].rstrip(path_linkage)

dirs = os.listdir(dpath)

if os.path.exists(dpath2) == False:
    os.mkdir(dpath2)

i = 0
for file in dirs:  
    print('file:',file)

    img = cv2.imread(dpath +  path_linkage + file)
    w = img.shape[0]
    h = img.shape[1]
    img = Image.new('RGB', (w, h), black)
    img.save(dpath2 + path_linkage + file)

    i += 1
    
