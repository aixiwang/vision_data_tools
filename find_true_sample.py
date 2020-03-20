#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

path = "data"
dirs = os.listdir(path)

for file in dirs:

    file2 = file.split('.')
    if file2[1] == 'bmp':
        print(file)
        if os.path.exists('data\\' + file2[0] + '.json') == False:
            print('find true sample:',file2[0] + '.bmp')
            os.system('move "data\\' + file2[0] + '.bmp"' + ' true_samples')
        else:
            print('find bmp & json:',file2[0] + '.json')
    
    if file2[1] == 'json':
        if os.path.exists('data\\' + file2[0] + '.bmp') == False:
            print('===========> has json, no bmp',file)
            os.system('del "data\\' + file2[0] + '.json"')