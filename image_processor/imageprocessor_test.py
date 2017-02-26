import imageprocessor
from imageprocessor import *

print("hello tester")

import unittest
from os import listdir
from os.path import isfile, join
import numpy as np
from PIL import Image


def test_folder(mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    cnt = 0
    blurry = 0
    var = 0
    for file in files:
        fp = open(mypath + "\\" + file, "rb")
        im = Image.open(fp)  # open from file object
        im.load()  # make sure PIL has read the data
        # with Image.open(mypath + "\\" + file) as im:
        if is_blurry(im):
            blurry = blurry + 1

        pil_image = im.convert('RGB')
        cv_image = np.array(pil_image)
        # Convert RGB to BGR
        cv_image = cv_image[:, :, ::-1].copy()
        var = var + variance_of_laplacian(cv_image)


        cnt = cnt + 1
        fp.close()
    print(var/cnt)
    return str(blurry) + "/" + str(cnt) + ": " + str(blurry / cnt)

class TestImageprocessor(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print ("something")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)



    def test_motion(self):
        mypath = "C:\\datasets\\motion"
        resp = "N/A"
        resp = test_folder(mypath)
        print("Motion: " + resp)

    def test_out_of_focus(self):
        mypath = "C:\\datasets\\out_of_focus_small"
        resp = "N/A"
        #resp = test_folder(mypath)
        print("Out of focus: " + resp)


if __name__ == '__main__':
    unittest.main()