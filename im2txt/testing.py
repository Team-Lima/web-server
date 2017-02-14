from tensorflow import gfile as gf
import base64 as b64
import binascii
import PIL.Image as image
from io import BytesIO

#reading the image
with gf.GFile("img.jpg", "r") as f:
    raw_data = f.read()

#encoding the data as b64

with open("b64.txt", "r") as f:
    b64_string = f.read()

img = image.open(BytesIO(b64.b64decode(b64_string)))

b64_raw = (img.tostring()).decode("utf-32")

#b64_bytes = b64.b64decode(b64_string)



#decoding the b64 string
#b64_raw = b64.b64decode(b64_string)

#with open("save.jpg", "wb") as f:
#    f.write(b64_raw)

if raw_data == b64_raw:
    print("Success")
else:
    print("Failure")


