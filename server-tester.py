import json
import urllib.request

test = 0

test_json = {
    "test": test
}

myurl = "http://localhost:5000/getjson"

print("Initialising request")

req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')

print("Gettint the JSON ready")

jsondata = json.dumps(test_json)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))

print("The JSON data is: ", jsondataasbytes)

print("Sending the request")

response = urllib.request.urlopen(req, jsondataasbytes)

print("The result is: ")
bytes_data = response.read()

print(bytes_data.decode("utf-8"))
