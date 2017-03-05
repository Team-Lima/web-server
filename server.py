from flask import Flask, jsonify, request
from image import ImageProcessor
import pandas as pd
from datetime import datetime as dt
from oauth2client import client, crypt

app = Flask(__name__)

columns = [
    "date",
    "success",
    "caption",
    "confidence",
    "dark",
    "blurry"
]



@app.route("/v1/caption", methods=["POST"])
def get_json():
    print("Received a request!")
    if request.method == "POST":
        print("It is a POST request!!")

        if request.is_json:
            print("It is a JSON !!!")
            #print("The data is: ", request.json)
            data = request.json
            if len(data) != 1 or (not "data" in data):
                print("Wrong JSON format")
                abort(400)
            else:
                print("Starting to run the image processor")
                result = run_image_processor(
                    img_b64=data["data"]
                )
                print("Successfully ran the image processor")
                return jsonify(result)

        else:
            print("Not a JSON")
            abort(400)


def run_image_processor(img_b64):
    """
        Function that takes the b64 version of the image, creates a new ImageProcessor object and returns
        the result of the image processing (i.e. the caption and improvement tips
    :param img_b64:     The image as a b64 string
    :return:            The results of the image processing
    """
    imageProcessor = ImageProcessor(
        img_id=0,
        img=img_b64
    )

    try:
        imageProcessor.run()
    except:
        print("ERROR while processing the image")

    result = imageProcessor.get_result()
    print(result)
    save_log(result)
    return result	

def save_log(data):
    df = pd.read_csv("tests/log.csv")
    new_entry = dict()
    new_entry["caption"]=data["data"]["text"]
    new_entry["success"]=data["success"]
    new_entry["confidence"]=data["data"]["confidence"]
    new_entry["date"] = str(dt.now())  
    new_entry["dark"] = "dark" in  data["data"]["improvementTips"]
    new_entry["blurry"] = "blurry" in data["data"]["improvementTips"]    
    data = list()
    for col in columns:
        data.append(str(new_entry[col]))
    data = [data]
    new_df = pd.DataFrame(data=data, columns=columns)
    df = df.append(new_df)
    df.to_csv("tests/log.csv", index=False)
    
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
    app.run(host="0.0.0.0",port=8000,debug=True)

