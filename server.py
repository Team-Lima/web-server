from flask import Flask, jsonify, request

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
            #print("The data is: ", request.json)
            data = request.json
            print(type(data))
        else:
            abort(400)

        return jsonify(test_dict)

if __name__ == "__main__":
    app.run(debug=True)