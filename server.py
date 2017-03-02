from flask import Flask, jsonify, request, Response
import image
import json
from exceptions import *
from oauth2client import client, crypt

app = Flask(__name__)

test_dict = {
    "test": "test",
    "more_test": {
        "inner-test": "mini-test"
    }
}


@app.route("/")
def index():
    print("I'm in!")


@app.route("/getjson", methods=["POST","GET"])
def get_json():
    print("Received a request!")
    if request.method == "POST":
        print("It is a POST request!!")

        if request.is_json:
            print("It is a JSON !!!")
            # print("The data is: ", request.json)
            data = request.json
            print(type(data))
        else:
            abort(400)

        return jsonify(test_dict)


@app.route("/v1/caption", methods=['POST'])
def caption():
    """
    function which is called by the HTTP POST request sent in by the client which returns a JSON string representing
    the classification result from the Neural Network

    :return: The JSON response formatted from the dictionary returned in process_image
    """
    if request.method == 'POST':
        # request from the application should be a JSON object of the form:
        json_req = request.json

        caption.counter += 1
        # send the data to the Neural network server
        try:
            image_processor = image.ImageProcessor(json_req['data'], caption.counter)

            js = json.dumps(image_processor.get_result())
            resp = Response(js, status=200, mimetype="application/json")

            return resp
        except (ImageException, NeuralNetworkFailure, ImageEncodingException, ImageProcessingException, ThreadMalfunctioningException) as e:
            print(e.msg)

caption.counter = 0


@app.route("/signin")
def signin():
    # (Receive token by HTTPS POST)
    token = request.form['idToken']
    CLIENT_ID = 'http://624718567609-ja0vbu5svh6l5q79pvtnk1rn3pjrrq2d.apps.googleusercontent.com/'
    try:
        idinfo = client.verify_id_token(token, CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")

    except crypt.AppIdentityError:
        pass
    userid = idinfo['sub']


if __name__ == "__main__":
    app.run()
