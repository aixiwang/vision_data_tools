#!/usr/bin/env python
#----------------------------------------------------------------------------------------
# convert labelme labels to segmentation masks
# 
# If your data is in "data" folder, you want to generate the dataset to "train" folder
# the "image" & "label" sub folder will be created in "train"
#
# Usage: python labelme2mask.py data train
# 
# 2020.3.10
# *added ploygon, circule, rectangle support
#-----------------------------------------------------------------------------------------
from __future__ import print_function

import argparse
import glob
import os
import os.path as osp
import sys
import cv2
import numpy as np
from PIL import Image, ImageDraw
import json
import math

black = (0, 0, 0)
white = (255, 255, 255)
defect_filter = ['p']

# Create an image with the data in the point_array array
def gen_label_img(filename, w, h, shapes, bgcolor, fgcolor):
    img = Image.new('RGB', (w, h), bgcolor)
    pixels = img.load()
    draw = ImageDraw.Draw(img)
    for shape in shapes:
        shape_t = shape['shape_type']
        points = shape['points']
        print('-----------------------------------')
        print('shape_t:',shape_t)
        if shape_t == 'polygon':
            
            #for polygon in points:
            #    print('polygon:',polygon)
            points2 = []
            for point in points:
                x = point[0]
                y = point[1]
                points2.append((float(x), float(y)))
                
            draw.polygon(points2, fill=fgcolor)
        
        if shape_t == 'circle':
            x1 = points[0][0]
            y1 = points[0][1]

            x2 = points[1][0]
            y2 = points[1][1]

            r = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

            eX, eY = 2*r, 2*r #Size of Bounding Box for ellipse

            bbox =  (x1 - eX/2, y1 - eY/2, x1 + eX/2, y1 + eY/2)
            draw.ellipse(bbox, fill=fgcolor)


        if shape_t == 'rectangle':
            x1 = points[0][0]
            y1 = points[0][1]

            x2 = points[1][0]
            y2 = points[1][1]

            bbox = ((x1,y1),(x2,y2))

            #print('bbox:',bbox)
            draw.rectangle(bbox, fill=fgcolor)
            

    img.save(filename)
    #s = input('any key to continue...')
        
def parse_json(label_file, labels):   
    print('parse json:',label_file,labels)

    try:    
        with open(label_file) as f:
            data = json.load(f)

        return 0, data['shapes']
    except Exception as e:
        print('parse json exception:',str(e))
        return -1, {}


#------------------
# main
#------------------
def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('input_dir', help='input annotated directory')
    parser.add_argument('output_dir', help='output dataset directory')

    args = parser.parse_args()

    if osp.exists(args.output_dir):
        print('Output directory already exists:', args.output_dir)
        #sys.exit(1)
        
    if os.path.exists(args.output_dir) == False:
        os.makedirs(args.output_dir)
        os.makedirs(osp.join(args.output_dir, 'image'))
        os.makedirs(osp.join(args.output_dir, 'label'))

    for filename in glob.glob(osp.join(args.input_dir, '*.json')):

        print('Generating dataset from:', filename)

        base = osp.splitext(osp.basename(filename))[0]
        out_img_file = osp.join(
            args.output_dir, 'image', base + '.png')

        out_png_file = osp.join(
            args.output_dir, 'label', base + '.png')

        if os.path.exists(out_png_file):
            print('label file has been generated, skip and continue:',out_png_file)
            continue

        if os.path.exists(filename.split('.')[0] + '.bmp'):
            img = cv2.imread(filename.split('.')[0] + '.bmp')
        if os.path.exists(filename.split('.')[0] + '.jpg'):
            img = cv2.imread(filename.split('.')[0] + '.jpg')
        if os.path.exists(filename.split('.')[0] + '.png'):
            img = cv2.imread(filename.split('.')[0] + '.png')
            
        cv2.imwrite(out_img_file,img)

        ret, shapes = parse_json(filename,defect_filter)
        if ret == 0:
            try:
                #print('shape_t:',shape_t,' detect_shapes:',defect_shapes) 
                gen_label_img(out_png_file,img.shape[1],img.shape[0],shapes,black,white)
            except Exception as e:
                print('gen_label_img exception:',str(e))
                pass


if __name__ == '__main__':
    main()
