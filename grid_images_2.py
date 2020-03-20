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
    print('usage: python grid_images2.py data_path')
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


#---------------------
# imcrop
#---------------------   
def imcrop(img, bbox): 
    x1,y1,x2,y2 = bbox
    if x1 < 0 or y1 < 0 or x2 > img.shape[1] or y2 > img.shape[0]:
        img, x1, x2, y1, y2 = pad_img_to_fit_bbox(img, x1, x2, y1, y2)
    print('y1:y2, x1:x2 ->',img.shape,y1,y2,x1,x2)
    return img[y1:y2, x1:x2]

#---------------------
# pad_img_to_fit_bbox
#---------------------   
def pad_img_to_fit_bbox(img, x1, x2, y1, y2):
    img = np.pad(img, ((np.abs(np.minimum(0, y1)), np.maximum(y2 - img.shape[0], 0)),
               (np.abs(np.minimum(0, x1)), np.maximum(x2 - img.shape[1], 0)), (0,0)), mode="constant")
    y1 += np.abs(np.minimum(0, y1))
    y2 += np.abs(np.minimum(0, y1))
    x1 += np.abs(np.minimum(0, x1))
    x2 += np.abs(np.minimum(0, x1))
    return img, x1, x2, y1, y2

#---------------------
# is_img_black
#---------------------
def is_img_black(img):
    w = img.shape[0]
    h = img.shape[1]
    blank_image = np.zeros((h,w,3), np.uint8)   
    return np.array_equal(blank_image,img)
    
    
    
i = 0
for file in dirs2:

    file2 = file.split('.')
    print('file:',file)
    
    if file2[1] != 'jpg' and file2[1] != 'bmp' and file2[1] != 'png':
        continue
        
    if file.find('_sub') < 0:
        image = cv2.imread(label_path + path_linkage + file)
        image2 = cv2.imread(image_path + path_linkage + file)

        h = image.shape[0]
        w = image.shape[1]
        
        # top, left
        bbox = (0,0,int(w/2-1),int(h/2-1))
        sub_img = imcrop(image,bbox)
        
        if is_img_black(sub_img) == False:
            sub_img2 = imcrop(image2,bbox)
            cv2.imwrite(label_path + path_linkage + file2[0] + '_sub0.' + file2[1],sub_img)
            cv2.imwrite(image_path + path_linkage + file2[0] + '_sub0.' + file2[1],sub_img2)
        else:
            print('skip top,left')
            
        # top, right
        bbox = (int(w/2),0,w-1,int(h/2-1))
        sub_img = imcrop(image,bbox)
        
        if is_img_black(sub_img) == False:
            sub_img2 = imcrop(image2,bbox)
            cv2.imwrite(label_path + path_linkage + file2[0] + '_sub1.' + file2[1],sub_img)
            cv2.imwrite(image_path + path_linkage + file2[0] + '_sub1.' + file2[1],sub_img2)
        
        else:
            print('skip top,right')
            
        # bottom, left
        bbox = (0,int(h/2),int(w/2),h-1)
        sub_img = imcrop(image,bbox)
        
        if is_img_black(sub_img) == False:
            sub_img2 = imcrop(image2,bbox)
            cv2.imwrite(label_path + path_linkage + file2[0] + '_sub2.' + file2[1],sub_img)
            cv2.imwrite(image_path + path_linkage + file2[0] + '_sub2.' + file2[1],sub_img2)
        
        else:
            print('skip bottom,left')
            
        # bottom, right
        bbox = (int(w/2),int(h/2),w-1,h-1)
        sub_img = imcrop(image,bbox)

        if is_img_black(sub_img) == False:
            sub_img2 = imcrop(image2,bbox)
            cv2.imwrite(label_path + path_linkage + file2[0] + '_sub3.' + file2[1],sub_img)
            cv2.imwrite(image_path + path_linkage + file2[0] + '_sub3.' + file2[1],sub_img2)
        else:
            print('skip bottom,right')
    
    i += 1
    
