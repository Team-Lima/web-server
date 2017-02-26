"""
server.py implements the server interface layer between the android client and the Neural network
"""

from flask import Flask
from flask import Response
from flask import json
from flask import Request

# file for parsing JSON
import json
# file containing the image processing code
import image
# import config
# import auth

# the flask application object with oauth integration
app = Flask(__name__)
# app.config.from_object(config.Config)

"""
Version 1 of the caption generation api - will return a caption for a given processed image
"""


@app.route("/v1/caption", methods=['POST'])
def caption():
    """
    function which is called by the HTTP POST request sent in by the client which returns a JSON string representing
    the classification result from the Neural Network

    :return: The JSON response formatted from the dictionary returned in process_image
    """
    if Request.method == 'POST':
        # request from the application should be a JSON object of the form:
        json_req = Request.json

        caption.counter += 1
        # send the data to the Neural network server
        image_processor = image.ImageProcessor(json_req['data'], caption.counter)

        js = json.dumps(image_processor.get_result())
        resp = Response(js, status=200, mimetype="application/json")
        return resp

caption.counter = 0

if __name__ == "__main__":
    app.run()



