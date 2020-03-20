#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------------------
# light equalizer
# 
#
#------------------------------------------
import os, sys
import cv2
import numpy as np
#import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print('usage: python light_equalizer.py data_path')
    sys.exit(-1)
    
if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'

dpath= sys.argv[1].rstrip(path_linkage)
dirs = os.listdir(dpath)
for file in dirs:
    print('file:',file)
    file2 = file.split('.')
    if (file2[1] == 'jpg' or file2[1] == 'bmp' or file2[1] == 'png'):

        img = cv2.imread(dpath + path_linkage + file, 0)

        #ret = cv2.equalizeHist(img)

        #plt.subplot(121)
        #plt.hist(img.ravel(), 256)
        #plt.subplot(122)
        #plt.hist(ret.ravel(), 256)
        #plt.show()
        #img = cv2.resize(img,(448,448))
        #ret = cv2.resize(ret,(448,448))

        #cv2.imshow('ret', np.hstack((img, ret)))
        #cv2.waitKey(0)


        clahe = cv2.createCLAHE(clipLimit=2.0,
                                tileGridSize=(8, 8))

        clahe = clahe.apply(img)
        img = cv2.resize(img,(448,448))
        #ret = cv2.resize(ret,(448,448))
        clahe = cv2.resize(clahe,(448,448))

        #cv2.imshow('imgs', np.hstack((img, ret, clahe)))
        cv2.imshow('imgs', np.hstack((img, clahe)))
        cv2.waitKey(0)
        #cv2.destroyAllWindows()
