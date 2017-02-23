"""
    File that declares the exceptions that are used in the server environment
"""

class ImageException(Exception):
    """
        Base class for exceptions raised when failing while
    """

    def __init__(self, id):
        """
            CONSTRUCTOR
        :param id:
        """
        self._id = id

    def get_image_id(self):
        """

        :return:    The id of the image that raised the exception
        """
        return self._id


class NeuralNetworkFailure(ImageException):
    """
        Exception raised if the neural network fails
    """

    def __init__(self, id):
        """
            CONSTRUCTOR
        :param id:      The id of the image that caused problems to the nn
        """
        super(id)
        self._msg = "The neural network failed!"

    def __str__(self):
        return self._msg


class ImageEncodingException(ImageException):
    """
        Exception raised if the b64 encoding is invalid
    """

    def __init__(self, id):
        """
            CONSTRUCTOR
        :param id:      the id of the image that is in the wrong format
        """
        super(id)
        self._msg = "The given image is not in a valid format"

    def __str__(self):
        return self._msg


class ImageProcessingException(ImageException):
    """
        Exception raised if there was an error while processing the image
    """

    def __init__(self, id):
        """
            CONSTRUCTOR
        :param id:      The id of the image that raised this exception
        """
        super(id)
        self._msg = "The image processor failed!"

    def __str__(self):
        return self._msg
