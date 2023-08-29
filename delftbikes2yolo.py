import os
import pandas as pd
from PIL import Image

YOLO_LABELS_PATH = "../datasets/DelftBikes/val/labels/"
VISANN_PATH = "../datasets/DelftBikes/val/annotations/"
VISIMG_PATH = "../datasets/DelftBikes/val/images/"

def convert(bbox, img_size):
    dw = 1/(img_size[0])
    dh = 1/(img_size[1])
    x = bbox[0] + bbox[2]/2
    y = bbox[1] + bbox[3]/2
    x = x * dw
    y = y * dh
    w = bbox[2] * dw
    h = bbox[3] * dh
    return (x,y,w,h) 

def ChangeToYolo():
    if not os.path.exists(YOLO_LABELS_PATH):
        os.makedirs(YOLO_LABELS_PATH)
    print(len(os.listdir(VISANN_PATH)))
    for file in os.listdir(VISANN_PATH):
        image_path = VISIMG_PATH + '/' + file.replace('txt', 'jpg')
        ann_file = VISANN_PATH + '/' + file
        out_file = open(YOLO_LABELS_PATH + '/' + file, 'w')
        bbox = pd.read_csv(ann_file,header=None).values
        img = Image.open(image_path)
        img_size = img.size
        for row in bbox:
        	label = convert(row[:4], img_size)
        	out_file.write(str(int(row[5]) - 1) + " " + " ".join(str(f'{x:.6f}') for x in label) + '\n')
        out_file.close()

if __name__ == '__main__':
    ChangeToYolo()
