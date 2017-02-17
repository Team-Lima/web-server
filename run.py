"""
    Runs the neural network and the image processing result
"""

from im2txt.im2txt import modified_run as nn_run
import base64 as b64
import server_util_functions


def process_image(img):
    """
        Processes the image and runs the nn and image processing on two different threads
    :param img:     The image as a base64 string
    :return:        The JSON response object containing the HTTP success status/code, the image caption, the confidence interval
                    and the list of error corrections
    """

    # Getting the image from b64 to a 'bytes' object
    bytes_img = b64.b64decode(img)

    # running the nn
    caption, prob = nn_run.run(bytes_img)

    # TODO: Determine the error corrections to be made to the image in the event of a low confidence interval returned

    # Return the JSON object collecting all the data from the Neural Network
    return server_util_functions.caption_res(True, True, 0, caption, prob, [])



