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
import server_util_functions


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
    a function to send the image data to the Neural network for classification and returns the caption string

    :param image: The base64 string representation of the image
    :return: A JSON response representing a textual description of the image classified by the Neural Network
    """



if __name__ == "__main__":
    app.run()



