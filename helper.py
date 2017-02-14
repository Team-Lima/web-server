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

