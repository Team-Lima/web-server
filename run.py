"""
    Runs the neural network and the image processing result
"""

from im2txt import run_inference as nn_run
import base64 as b64
import _thread as thread

class ImageProcessor:
    """
        Class that represents the image processor
    """

    def __init__(self, img):
        """

        :param img:     The image to be processed, as a base64 string
        """
        self._b64_img = str(img)
        self.result = dict()

    def _get_caption(self):
        """
            Inner function that calls the neural network and
        :return:    -
        """
        try:
            # Getting the image from b64 to a 'bytes' object
            bytes_img = b64.b64decode(self._b64_img)
            print(bytes_img)
            # running the nn
            caption, prob = nn_run.predict(bytes_img)
        except Exception:
            # Should not be the case, but just to be safe
            print("The neural network failed!")
            #TODO: Figure out what the defined behaviour should be here

    def _get_image_faults(self):
        """
            Inner function that calls the actual image processor and gets the feedback from it
        :return:        -
        """
        #TODO: 


