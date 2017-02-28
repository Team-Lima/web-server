"""
server.py implements the server interface layer between the android client and the Neural network
"""

import flask
from flask import Response
from flask import json
from flask import Request
from exceptions import *
import server_util_functions

from oauth2client import client
import httplib2
import json
import image


# the flask application object with oauth integration
app = flask.Flask(__name__)

"""
Version 1 of the caption generation api - will return a caption for a given processed image
"""


@app.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(
        # TODO: Will need to supply a client_secrets.json file containing the client_id and secret_id
        'client_secrets.json',
        # TODO: add the uris for Google apis in use
        scope='',
        redirect_uri=flask.url_for('oauth2callback', _external=True),
        include_granted_scopes=True)
    if 'code' not in flask.request.args:
        auth_uri = flow.step1_get_authorize_url()
        return flask.redirect(auth_uri)
    else:
        auth_code = flask.request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        flask.session['credentials'] = credentials.to_json()
        return flask.redirect(flask.url_for('caption'))


@app.route("/v1/caption", methods=['POST'])
def caption():
    """
    function which is called by the HTTP POST request sent in by the client which returns a JSON string representing
    the classification result from the Neural Network

    :return: The JSON response formatted from the dictionary returned in process_image
    """
    if Request.method == 'POST':
        if 'credentials' not in flask.session:
            return flask.redirect(flask.url_for('oauth2callback'))
        credentials = client.OAuth2Credentials.from_json(flask.session['credentials'])
        if credentials.access_token_expired:
            return flask.redirect(flask.url_for('oauth2callback'))
        else:
            http_auth = credentials.authorize(httplib2.Http())
            # request from the application should be a JSON object of the form:
            json_req = Request.json

            caption.counter += 1
            # send the data to the Neural network server
            try:
                image_processor = image.ImageProcessor(json_req['data'], caption.counter)

                js = json.dumps(image_processor.get_result())
                resp = Response(js, status=200, mimetype="application/json")
                return resp
            except (ImageException, NeuralNetworkFailure, ImageEncodingException, ImageProcessingException, ThreadMalfunctioningException):
                # TODO: send back failure response to the client
                pass

            # js = json.dumps(server_util_functions.caption_res(True, True, 200, "Definitely something", 0.5, []))
            # resp = Response(js, status=200, mimetype="application/json")
            # return resp

caption.counter = 0

if __name__ == "__main__":
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug = False
    app.run()



