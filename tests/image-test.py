import image as img
import base64 as b64
import os
from PIL import Image
import tensorflow as tf

def get_b64_fromtxt(filename):

    with open(filename, "r") as f:
        b64_data = f.read()

    print(type(b64_data))
    return b64_data

def get_b64(filename):
    """

    :param filename:        The name of the image file that we want to read
    :return:                The image as a b64 string
    """

    with tf.gfile.GFile(filename, "r") as f:
        image = f.read()
        b64_data = b64.b64encode(image)

    b64_data = b64_data.decode()
    print(b64_data)
    print(type(b64_data))
    return b64_data

def run_tests():
    """

    :return:            -
    """
    idx = 0


    b64_img = get_b64("testing/images/responsive-blurry-images-wordpress.jpg")

    image_processor = img.ImageProcessor(b64_img, idx)

    image_processor.run()

    print(image_processor.get_result())

if __name__ == "__main__":
    run_tests()

