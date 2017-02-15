"""
server.py implements the server interface layer between the android client and the Neural network
"""

from flask import Flask
from flask import Response
from flask import json
from flask import Request

# file for parsing JSON
import json
# file of helper functions for constructing the JSON messages
import helper


# the flask application object
app = Flask(__name__)

"""
Version 1 of the caption generation api - will return a caption for a given processed image
"""


@app.route("/v1/caption", methods=['POST'])
def caption():
    """
    :return:
    """
    if Request.method == 'POST':
        # request from the application should be a JSON object of the form:
        json_req = Request.json

        # send the data to the Neural network server
        result = send_image(json_req['data'])

        js = json.dumps(result)
        resp = Response(js, status=200, mimetype="application/json")
        return resp


def send_image(image):
    """
    :param image: The base64 string representation of the image
    :return: A JSON response representing a textual description of the image classified by the Neural Network
    """
    
    return helper.caption_res(True, 0, "a thing of some sort...", 1.0, [])

if __name__ == "__main__":
    app.run()



