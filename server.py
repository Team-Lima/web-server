"""
server.py implements the server interface layer between the android client and the Neural network
"""

from flask import Flask
import json #file for parsing JSON
import helper #file of helper functions for constructing the JSON messages


app = Flask(__name__)

"""
Version 1 of the caption generation api - will return a caption for a given processed image

Will need to determine what data is being sent to the server via this call
"""


@app.route("/v1/caption")
def caption():
    """
    :return: A JSON object representing the image classification response as a string
    """
    return json.dumps(helper.caption_res(True, 0, "a thing of some sort...", 1.0, []))


if __name__ == "__main__":
    app.run()



