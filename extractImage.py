# -*- coding: utf-8 -*-

import h5py as hp
from PIL import Image, ImageDraw
import os

def DrawBoxes(draw, bb, color):
    for i in range(0, bb.shape[2]):
        box = bb[:, :, i]
        path = []
        for j in range(0, box.shape[1]):
            pos = box[:, j]
            path.append(pos[0])
            path.append(pos[1])
            
        path.append(box[0, 0])
        path.append(box[1, 0])
        
        draw.line(path, color, 1)

def ExtractFiles(h5path, output_dir):
    file = hp.File(h5path, 'r')
    data = file['data']
    for key in data.keys():
        image = data[key]
        charbb = image.attrs['charBB']
        wordbb = image.attrs['wordBB']
        image = Image.fromarray(image[:])
        draw = ImageDraw.Draw(image)
        DrawBoxes(draw, charbb, 'red')
        DrawBoxes(draw, wordbb, 'blue')       
        image.save(os.path.join(output_dir, key+ '.jpg'))
        
if __name__ == '__main__':
    ExtractFiles('./results/SynthText.h5', './results/viz')
