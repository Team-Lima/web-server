"""
server_util_functions.py contains the helper functions which aid in request decoding and response construction
"""


def caption_res(success, data_success, status, text, confidence, improvement_tips):
    """
    a function to create JSON messages given data from the Neural Network in order to send to the client

    :param success: Whether the HTTP request was successful or not in being sent/recieved
    :param status: The HTTP status code
    :param data_success: The Neural Network classification success indicator
    :param text: The string description of the image as classified by the Neural Network
    :param confidence: The confidence interval value represented as a floating point number between 1.0 and 0.0
    associated with the classification
    :param improvement_tips: a list of actions to be performed by the client to correct the image
    :return: A JSON object containing the information above
    """

    return {
        "success": success,
        "status": status,
        "data": {
            "text": text,
            "success":  data_success,
            "confidence": confidence,
            "improvementTips": improvement_tips
        }
    }


