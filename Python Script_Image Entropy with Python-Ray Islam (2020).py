# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
os.getcwd()

#pip install opencv-python

import cv2
from matplotlib import pyplot as plt
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import img_as_ubyte

image1 = cv2.imread("images/Ray.jpg", 0)
image2 = cv2.imread("images/riga_from_satellite.jpg", 1)

cv2.imshow("Grey image", image1)
#cv2.imshow("Color image", image2)

cv2.waitKey(0)
cv2.destroyAllwindows()

image1.ndim

entropy_image1 = entropy(image1, disk(10))
plt.imshow(entropy_image1)

from skimage.filters import threshold_otsu
thresh = threshold_otsu(entropy_image1)
binary = entropy_image1 <= thresh
plt.imshow(binary)
