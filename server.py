from flask import Flask, jsonify, request
from image import ImageProcessor

app = Flask(__name__)

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
    return result	

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)

