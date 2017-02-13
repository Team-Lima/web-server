"""
helper.py contains the helper functions which aid in request decoding and response construction
"""


def caption_res(success, status, text, confidence, improvement_tips):
    """
    :param success:
    :param status:
    :param text:
    :param confidence:
    :param improvement_tips:
    :return:
    """

    return {
        "success": success,
        "status": status,
        "data": {
            "text": text,
            "confidence": confidence,
            "improvementTips": improvement_tips
        }
    }


def caption_req(json_data):
    """
    :param json_data: a text string representing the json data passed to the server from the client
    :return: the JSON object associated with the text string
    """
    return
