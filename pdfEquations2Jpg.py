#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:37:23 2022

@author: stefano
"""

import pdf2image 
import os
import matplotlib.pyplot as plt
#from PIL import Image
from skimage import io
import numpy as np

path = '/home/stefano/Documents/thatIt/'
os.chdir(path)
pages = pdf2image.convert_from_path('thatIt.pdf')

for i in range(len(pages)):
	pages[i].save('page'+ str(i) +'.jpg', 'JPEG')
    
#img = Image.open('page0.jpg')
image = io.imread('page0.jpg')

u = np.where(image[:1500,:,:] != 255)

j = 0
x_min = min(u[j])
x_max = max(u[j])

j = 1
y_min = min(u[j])
y_max = max(u[j])

plt.imshow(image[x_min:x_max, y_min:y_max, :])
plt.savefig('prova.png')