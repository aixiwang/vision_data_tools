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

if len(sys.argv) != 2:
    print('usage: python color2gray_images.py data_path')
    sys.exit(-1)
    
    
if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'


dpath = sys.argv[1].rstrip(path_linkage)
    

dirs = os.listdir(dpath)

#data_n = len(dirs)
#n1 = data_n
#print('n1:',n1)


    
i = 0
for file in dirs:
    file2 = file.split('.')
    if file.find('gray_') < 0 and (file2[1] == 'jpg' or file2[1] == 'bmp' or file2[1] == 'png'):
        image = cv2.imread(dpath + path_linkage + file)
        
        print('file:',file,image.shape)
        #h = image.shape[0]
        #w = image.shape[1]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        cv2.imwrite(dpath + '\\' + 'gray_' + file2[0] + '_sub2.' + file2[1],gray)

    
    i += 1
    
