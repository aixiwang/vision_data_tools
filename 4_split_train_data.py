#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------------------
# split_train_data
# 
#
# run on windows
#------------------------------------------
import os, sys

if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'

#dpath = "textile_seg_dataset"
train_percentage = 0.9
val_percentage = 0.1

if len(sys.argv) != 2:
    print('usage: python split_train_data.py data_path')
    sys.exit(-1)
    
dpath = sys.argv[1].rstrip(path_linkage)

# change path if you want to run on Linux
train_image = dpath + '%strain%simage%s' % (path_linkage)
train_label = dpath + '%strain%slabel%s' % (path_linkage)
val_image = dpath + '%sval%simage%s' % (path_linkage)
val_label = dpath + '%sval%slabel%s' % (path_linkage)

if os.path.exists(dpath + path_linkage + 'val') == False:
    os.mkdir(dpath + path_linkage + 'val')


if os.path.exists(val_image) == False:
    os.mkdir(val_image)
    
if os.path.exists(val_label) == False:
    os.mkdir(val_label)

dirs = os.listdir(train_image)

data_n = len(dirs)
n1 = int(data_n/int(data_n * val_percentage))
print('n1:',n1)


i = 0
for file in dirs:
    if (i % n1 == 0):
    
        print('move file:',file)
        if os.path.exists(val_image + file) == False:
            print(train_image + file + ' -> ' + val_image + file)
            if os.name == "posix":
                os.system('mv "' + train_image + file + '"  "' + val_image +  file + '"')
            else:
                os.system('move "' + train_image + file + '"  "' + val_image +  file + '"')
            
        if os.path.exists(val_label + file) == False:
            print(train_label + file + ' -> ' + val_label + file)
            
            if os.name == "posix":
                os.system('mv "' + train_label + file + '"  "' + val_label +  file + '"')
            else:
                os.system('move "' + train_label + file + '"  "' + val_label +  file + '"')
                
        #s = input('any key ...')
        
    i += 1
    
    
