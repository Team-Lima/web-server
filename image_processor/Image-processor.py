import PIL
from PIL import Image, ImageFilter
import os
import io

from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image


'''Returns the brightness ratio: 1 means completely white, 0 means completely black'''
def get_ratio (im):
    one_pixel = im.resize((1,1), PIL.Image.ANTIALIAS) # resizing the image to one pixels
    rgb_im = one_pixel.convert('RGB') # converting it to RGBs
    r, g, b = rgb_im.getpixel((0, 0)) # getting r, b, b values
    ratio = (r+g+b)/(255*3.0) # determining the ratio
    return ratio


# Testing
print ("Hello")
im0 = Image.open( 'p0.jpg' )
imshow(np.asarray(im0))
print (get_ratio(im0))

