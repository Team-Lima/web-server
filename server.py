"""
server.py implements the server interface layer between the android client and the Neural network
"""

from flask import Flask
import json


app = Flask(__name__)


@app.route("/")
def hello():
    return "hello Neural Guide!"


def caption_res(success, status, text, confidence, improvement_tips):
    return {
        "success": success,
        "status": status,
        "data": {
            "text": text,
            "confidence": confidence,
            "improvementTips": improvement_tips
        }
    }


"""
Version 1 of the caption generation api - will return a caption for a given processed image
"""
@app.route("/v1/caption")
def caption():
    return json.dumps(caption_res(True, 0, "a thing of some sort...", 1.0, []))


if __name__ == "__main__":
    app.run()



