#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:37:23 2022

@author: stefano
"""

import pdf2image 
import os
#import matplotlib.pyplot as plt
#from PIL import Image
import imageio
from skimage import io
import numpy as np

path = '/home/stefano/Documents/thatIt/'
os.chdir(path)
name = 'formula'
pages = pdf2image.convert_from_path(name + '.pdf')

for i in range(len(pages)):
	pages[i].save(name +'.jpeg', 'JPEG')
image = io.imread(name + '.jpeg')

#u = np.where(image[:1500,:,:] != 255)
u = np.where(image != 255)

j = 0
y_min = min(u[j]) - 5
y_max = max(u[j]) + 5


j = 1
x_min = min(u[j]) - 5
x_max = max(u[j]) + 5

ku = image[y_min:y_max, x_min:x_max, :]

#plt.imshow(ku)
imageio.imwrite(name + '.jpeg', ku)

os.remove(name + '.aux')
os.remove(name + '.log')
os.remove(name + '.pdf')