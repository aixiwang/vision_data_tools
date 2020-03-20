#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------------------
# grid_images_2
# * remove no defect samples from sub_imgs
#
# run on windows
#------------------------------------------
import os, sys
import cv2
import numpy as np

if len(sys.argv) != 2:
    print('usage: python grid_images.py data_path')
    sys.exit(-1)

if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'

dpath = sys.argv[1].rstrip(path_linkage)
image_path = dpath + path_linkage + 'image'
label_path = dpath + path_linkage + 'label'

dirs2 = os.listdir(label_path)

#data_n = len(dirs)
#n1 = data_n
#print('n1:',n1)

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
    


for file in dirs2:

    if file.find('_sub') < 0:
        image = cv2.imread(label_path + path_linkage + file)
        image2 = cv2.imread(image_path + path_linkage + file)

        file2 = file.split('.')
        print('file:',file,image.shape)
        h = image.shape[0]
        w = image.shape[1]
        
        
        if (h != 1536 or w != 2048):
            continue
        
        
        #          
        #  0,1,2,3  => i
        #  4,5,6,7
        #  8,9,10,11
        #        |
        #        j
        
        for i in range(0,4):
            for j in range(0,3):
                k = j*i + i
            
            
                bbox = (i*512,j*512,(i+1)*512,(j+1)*512)
                
                print('i,j,k,bbox:',i,j,k,bbox)
                
                
                sub_img = imcrop(image,bbox)
                
                if sum(sum(sum(sub_img))) > 0:
                    sub_img2 = imcrop(image2,bbox)
                    #cv2.imwrite(label_path + path_linkage + 'new_' + file2[0] + '_sub%d.' % (k) + file2[1],sub_img)
                    cv2.imwrite(image_path + path_linkage + 'new_' + file2[0] + '_sub%d.' % (k) + file2[1],sub_img2)
                else:
                    print('skip index:',k)

        
