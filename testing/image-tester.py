import image as img
import base64 as b64
import os

def get_b64(filename):
    """

    :param filename:        The name of the image file that we want to read
    :return:                The image as a b64 string
    """
    with open(filename, "r") as f:
        result = b64.b64encode(f.read())

    return result

def run_tests():
    """

    :return:            -
    """
    for image in os.listdir("testing/images"):

        b64_img = get_b64("testing/images/"+image.__str__())


if __name__ == "__main__":
    run_tests()

