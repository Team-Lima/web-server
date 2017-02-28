from im2txt import run_inference as nn_run
import base64 as b64
import _thread as thread
from exceptions import *
from PIL import Image
from io import BytesIO
from image_processor import imageprocessor as ip


class ImageProcessor:
    """
        Class that represents the image processor
    """

    def __init__(self, img, img_id):
        """

        :param img:     The image to be processed, as a base64 string
        :param img_id:  The id of the image
        """
        self._b64_img = str(img)
        self._img_id = img_id

        self._success_caption = True
        self._success_faults = True

    def _get_caption(self, bytes_img):
        """
            Inner function that calls the neural network and

        :param bytes_img:                   The image that will be passed to the nn, as a bytes object
        :return:                            -
        :raises NeuralNetworkFailure:       If the neural network fails for any reason
        """
        try:

            # running the nn
            self._caption, self._prob = nn_run.predict(bytes_img)
        except Exception:
            # Should not be the case, but just to be safe
            self._success_caption = False
            raise NeuralNetworkFailure(self._img_id)

    def _get_image_faults(self, img):
        """
            Inner function that calls the actual image processor and gets the feedback from it
        :param img:                             The image to be processed, as a PIL object

        :return:                                -
        :raises ImageProcessingException:       If the image processing failed
        """
        try:
            #self._problems = ip.image_problems(img)
            self._tips = ip.image_problems(img)
        except Exception:
            # Should not be the case, but just to be safe
            self._success_faults = False
            raise ImageProcessingException(self._img_id)

    def run(self):
        """
            Method that runs the image processor and caption generator

        :return:   -
        :raises ImageEncodingException:     if the image is corrupted(i.e. the b64 string can't be processed)
        :raises ThreadMalfunctionException:     If a thread crashes for some reason
        """
        try:
            # Getting the image from b64 to a 'bytes' object
            bytes_img = b64.b64decode(self._b64_img)
            print(bytes_img)
        except:
            #Should not happen, but just to be safe
            raise ImageEncodingException(self._img_id)


        try:
            #Getting the PIL Image object out of the b64 string
            PIL_img = Image.open(BytesIO(bytes_img))
        except:
            raise ImageEncodingException(self._img_id)


        #setting up the 2 threads
        try:
            """
                The neural network will be run on the main thread, while the image processing part
            will run o a separate one.
            """
            # (1) running the image processor
            self._get_image_faults(PIL_img)


            # (2) running the neural network(i.e. caption generator)
            self._get_caption(bytes_img)
        except:
            raise ThreadMalfunctioningException()

    def get_result(self):
        """

        :return:    the results of the image processor, as a dictionary, with the following structure:
        """
        result = dict()

        result = {
            "success": self._success_faults and self._success_caption,
            "status": 0,
            "data": {
                "text": self._caption,
                "confidence": self._prob,
                "improvementTips": self._tips
            }
        }

        return result
