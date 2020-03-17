#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------------------
# copy new files from src to desc
# 
#
# run on linux/windows
#------------------------------------------
import os, sys

#dpath = "textile_seg_dataset"

if len(sys.argv) != 3:
    print('usage: python copy_files.py src_path desc_path')
    sys.exit(-1)

if os.name == "posix":
   path_linkage = '/'
else:
   path_linkage = '\\'

dpath1 = sys.argv[1].rstrip(path_linkage)
dpath2 = sys.argv[2].rstrip(path_linkage)
    
dirs = os.listdir(dpath1)

for file in dirs:
    print('file:',file)
    
    if os.path.exists(dpath2 + path_linkage + file) == False:
            print('copy file:',file)
            
            src_file_path = '"' + dpath1 + path_linkage + file + '"'
            desc_file_path = dpath2 
            if os.name == "posix":
                os.system('cp ' + src_file_path + ' ' + desc_file_path)
            else:
                os.system('copy ' + src_file_path + ' ' + desc_file_path)


