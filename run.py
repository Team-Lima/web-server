"""
    Runs the neural network and the image processing result
"""

from im2txt.im2txt import modified_run as nn_run
import base64 as b64

def process_image(img):
    """
        Processes the image and runs the nn and image processing on two different threads
    :param img:     the image as a base64 string
    :return:
    """

    # Getting the image from b64 to a 'bytes' object
    bytes_img = b64.b64decode(img)

    #running the nn
    caption, prob = nn_run.run(bytes_img)



