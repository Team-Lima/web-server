import PIL
from PIL import Image, ImageFilter
import os
import io

from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image


'''Returns the brightness ratio: 1 means completely white, 0 means completely black'''
def get_darkness_ratio (im):
    one_pixel = im.resize((1,1), PIL.Image.ANTIALIAS) # resizing the image to one pixels
    rgb_im = one_pixel.convert('RGB') # converting it to RGBs
    r, g, b = rgb_im.getpixel((0, 0)) # getting r, b, b values
    ratio = (r+g+b)/(255*3.0) # determining the ratio
    return ratio


import cv2
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


def display(img):
    screen_res = 1280, 720
    scale_width = screen_res[0] / img.shape[1]
    scale_height = screen_res[1] / img.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)

    cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('dst_rt', window_width, window_height)

    cv2.imshow('dst_rt', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def image_problems(image):
    list = []
    if get_darkness_ratio(image) < 0.3:
        list.append("too_dark")
    pil_image = image.convert('RGB')
    cv_image = np.array(pil_image)
    # Convert RGB to BGR
    cv_image = cv_image[:, :, ::-1].copy()

    #display(cv_image)

    if variance_of_laplacian(cv_image) < 100:
        list.append("out_of_focus")
    return list








# Testing
im = Image.open( 'r1.jpg' )
print (image_problems(im))