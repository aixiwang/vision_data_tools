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
from PIL import Image, ImageDraw

black = (0, 0, 0)
white = (255, 255, 255)

#dpath = "textile_seg_dataset"
train_percentage = 0.7
val_percentage = 0.3

if len(sys.argv) != 4:
    print('usage: python grid_images.py data_path desc_path result_path')
    sys.exit(-1)

if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'

dpath = sys.argv[1].rstrip(path_linkage)
dpath2 = sys.argv[2].rstrip(path_linkage)
dpath3 = sys.argv[3].rstrip(path_linkage)

dirs = os.listdir(dpath3)

if os.path.exists(dpath2) == False:
    os.mkdir(dpath2)

    
#---------------------
# is_img_black
#---------------------
def is_img_black(img):
    w = img.shape[0]
    h = img.shape[1]
    blank_image = np.zeros((h,w,3), np.uint8)   
    return np.array_equal(blank_image,img)
    
    
    
i = 0
for file in dirs:  
    print('file:',file)
    file2 = file.split('.')
    
    img = cv2.imread(dpath3 +  path_linkage + file)
    w = img.shape[0]
    h = img.shape[1]
    if is_img_black(sub_img):
        # nothing was detected, this is the one we want to copy

        p1 = dpath + path_linkage + file2[0].rstrip('_predict') + '.jpg'
        p2 = dpath + path_linkage + file2[0].rstrip('_predict') + '.bmp'
        p3 = dpath + path_linkage + file2[0].rstrip('_predict') + '.png'
        print('p1:',p1)
        print('p2:',p2)
        print('p3:',p3)

        if os.path.exists(p1):
            print('p1:',p1)
            p4 = p1
            
        elif os.path.exists(p2):
            print('p2:',p2)
            p4 = p2
            
        elif os.path.exists(p3):
            print('p3:',p3)
            p4 = p3
        else:
            print('can not find source file,exit')
            sys.exit(-1)
            
        # copy image file
        print('copy image file:',p4)        
        if os.name == "posix":  
            os.system('cp "' + p4 + '" ' + dpath2)
        else:
            os.system('copy "' + p4 + '" ' + dpath2)
            

        p4 = dpath + path_linkage + file2[0].rstrip('_predict') + '.json'
        
        if os.path.exists(p4):        
            # copy json file
            print('copy json file:',p4)
            if os.name == "posix":  
                os.system('cp "' + p4 + '" ' + dpath2)
            else:
                os.system('copy "' + p4 + '" ' + dpath2)
            
                        
    #img = Image.new('RGB', (w, h), black)
    #img.save(dpath2 + path_linkage + file)

    i += 1
    
