#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------------------
# move_unlabled to "to_be_labeld" folder
# 
#
# run on windows
#------------------------------------------
import os, sys

#dpath = "textile_seg_dataset"

if len(sys.argv) != 2:
    print('the unlabeled files will be move to to_be_labeld folder')
    print('usage: python find_true_sample.py data_path')
    sys.exit(-1)


if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'


dpath = sys.argv[1].rstrip(path_linkage)
    
dirs = os.listdir(dpath)
os.mkdir('to_be_labeld')

for file in dirs:
    print('file:',file)
    file2 = file.split('.')
    
    print('file2[1]:',file2[1])
    if file2[1] == 'bmp' or file2[1] == 'jpg' or file2[1] == 'png':
        print(file)
        if os.path.exists( dpath + path_linkage + file2[0] + '.json') == False:
            print('find unlabeled sample:',file2[0] + '.' + file2[1])
            if os.name == "posix":
                os.system('mv "' + dpath + path_linkage + file2[0] + '.' + file2[1] + '"' + ' to_be_labeld')
            else:
                os.system('move "' + dpath + path_linkage + file2[0] + '.' + file2[1] + '"' + ' to_be_labeld')
            
        else:
            print('find bmp & json:',file2[0] + '.json')
    
    if file2[1] == 'json':
        if  os.path.exists(dpath + path_linkage + file2[0] + '.bmp') == False:
            if  os.path.exists(dpath + path_linkage + file2[0] + '.jpg') == False:
                if  os.path.exists(dpath + path_linkage + file2[0] + '.png') == False:
                    print('===========> has json, no image file',file)
                    if os.name == "posix":                    
                        os.system('rm "' + dpath + path_linkage + file2[0] + '.json"')
                    else:
                        os.system('del "' + dpath + path_linkage + file2[0] + '.json"')
                    
