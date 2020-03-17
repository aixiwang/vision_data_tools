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


    
dirs = os.listdir('image')
dirs2 = os.listdir('label')

for file in dirs:
    print('file:',file)
    
    if os.path.exists('label\\' + file) == False:
            print('no label,will del the image:',file)
            os.system('del "image\\' + file)
    
            s = input('...')

for file in dirs2:
    print('file2:',file)
    
    if os.path.exists('image\\' + file) == False:
            print('no image,will del the label:',file)
            os.system('del "label\\' + file)
            s = input('...')
