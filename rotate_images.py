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
import imutils

#dpath = "textile_seg_dataset"
train_percentage = 0.7
val_percentage = 0.3

if len(sys.argv) != 2:
    print('usage: python grid_images.py data_path')
    sys.exit(-1)

if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'


dpath = sys.argv[1].rstrip(path_linkage)
dirs = os.listdir(dpath)

def imcrop(img, bbox): 
    x1,y1,x2,y2 = bbox
    if x1 < 0 or y1 < 0 or x2 > img.shape[1] or y2 > img.shape[0]:
        img, x1, x2, y1, y2 = pad_img_to_fit_bbox(img, x1, x2, y1, y2)
    print('y1:y2, x1:x2 ->',img.shape,y1,y2,x1,x2)
    return img[y1:y2, x1:x2]

def pad_img_to_fit_bbox(img, x1, x2, y1, y2):
    img = np.pad(img, ((np.abs(np.minimum(0, y1)), np.maximum(y2 - img.shape[0], 0)),
               (np.abs(np.minimum(0, x1)), np.maximum(x2 - img.shape[1], 0)), (0,0)), mode="constant")
    y1 += np.abs(np.minimum(0, y1))
    y2 += np.abs(np.minimum(0, y1))
    x1 += np.abs(np.minimum(0, x1))
    x2 += np.abs(np.minimum(0, x1))
    return img, x1, x2, y1, y2

    
i = 0
for file in dirs:  
    if file.find('_rotation') < 0:
        print('file:',file)

        image = cv2.imread(dpath + path_linkage + file)
        file2 = file.split('.')
        print('file:',file,image.shape)
        h = image.shape[0]
        w = image.shape[1]
        

        rotated90 = imutils.rotate_bound(image, 90)
        rotated180 = imutils.rotate_bound(image, 180)
        rotated270 = imutils.rotate_bound(image, 270)
        
        cv2.imwrite(dpath + path_linkage + file2[0] + '_rotation_0.' + file2[1],rotated90)
        cv2.imwrite(dpath + path_linkage + file2[0] + '_rotation_1.' + file2[1],rotated180)
        cv2.imwrite(dpath + path_linkage + file2[0] + '_rotation_2.' + file2[1],rotated270)

    i += 1
    
