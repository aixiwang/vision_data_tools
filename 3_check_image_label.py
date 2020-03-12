#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------------------
#
# check image & label folder to make sure 1 image exists, 
# then 1 label exists, otherwise clean it
#------------------------------------------
import os, sys

dpath = '.'
if len(sys.argv) != 2:
    print('usage: python xx.py data_path')
    sys.exit(-1)


if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'


dpath = sys.argv[1].rstrip(path_linkage)



    
dirs = os.listdir(dpath + path_linkage + 'image')
dirs2 = os.listdir(dpath + path_linkage + 'label')

print('image files:',len(dirs))
print('label files:',len(dirs2))

s = input('...')

for file in dirs:
    print('file:',file)
    
    if os.path.exists(dpath + path_linkage + 'label' + path_linkage + file) == False:
            print('no label,will del the image:',file)
            if os.name == "posix":
                os.system('rm "' + dpath + path_linkage + 'image' + path_linkage + file + '"')
            else:
                os.system('del "' + dpath + path_linkage + 'image' + path_linkage + file + '"')

            s = input('...')

for file in dirs2:
    print('file2:',file)
    
    if os.path.exists(dpath + path_linkage + 'image' + path_linkage + file) == False:
            print('no image,will del the label:',file)
            if os.name == "posix":            
                os.system('rm "' + dpath + path_linkage + 'label' + path_linkage + file + '"')
            else:
                os.system('del "' + dpath + path_linkage + 'label' + path_linkage + file + '"')
            
            s = input('...')
