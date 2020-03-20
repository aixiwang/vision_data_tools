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

if len(sys.argv) != 3:
    print('usage: python color2gray_images2.py src_path desc_path')
    sys.exit(-1)
    
if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'

src_path = sys.argv[1].rstrip(path_linkage)
desc_path = sys.argv[2].rstrip(path_linkage)    

if os.path.exists(desc_path) == False:
    os.mkdir(desc_path)

dirs = os.listdir(src_path)

#data_n = len(dirs)
#n1 = data_n
#print('n1:',n1)
    
i = 0
for file in dirs:

    file2 = file.split('.')
    print('file:',file)
    
    if file2[1] != 'jpg' and file2[1] != 'bmp' and file2[1] != 'png':
        continue
        
    #if file.find('_sub') < 0:
    if 1: 
        image = cv2.imread(src_path + path_linkage + file)
        
        print('file:',file,image.shape)
        #h = image.shape[0]
        #w = image.shape[1]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        color = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        cv2.imwrite(desc_path + path_linkage + file,color)

    
    i += 1
    
