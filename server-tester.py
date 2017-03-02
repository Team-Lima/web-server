import json
import urllib.request
import tensorflow as tf
import base64 as b64


def get_b64(filename):
    """

    :param filename:        The name of the image file that we want to read
    :return:                The image as a b64 string
    """

    with tf.gfile.GFile(filename, "r") as f:
        image = f.read()
        b64_data = b64.b64encode(image)

    b64_data = b64_data.decode()
    #print(b64_data)
    #print(type(b64_data))
    return b64_data


def post_request(output):
    myurl = "http://localhost:80/getjson"

    print("Initialising request")

    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    print("Getting the JSON ready")

    jsondata = json.dumps(output)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))

    #print("The JSON data is: ", jsondataasbytes)

    print("Sending the request")

    response = urllib.request.urlopen(req, jsondataasbytes)

    print("The result is: ")
    bytes_data = response.read()

    print(bytes_data.decode("utf-8"))

def main():

    image_path = "testing/images/1.jpg"
    print("Getting base64")
    output = dict()
    output["data"] = b64_data = get_b64(image_path)
    print("Encoded image")
    post_request(output)

if __name__ == "__main__":
    main()
