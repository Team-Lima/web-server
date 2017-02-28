### Synopsis

The server layer for the Neural Guide application

### Dependencies

(1) _Python3.6_  <br /> <br />
(2) _PIL_ 
```
pip3 install pillow
```
(3) _OpenCV 3.0_ <br />
    See install instructions for Mac OS/ Linux [here](http://tsaith.github.io/install-opencv-3-for-python-3-on-osx.html)
    <br />  <br />
(4) _TensorFlow 0.12.0_ <br />
      **IMPORTANT** : It has to be 0.12.0 or any version **below** Tensorflow 1 for this code to work
      <br />
      You can download the wheel file to install this version [here](https://www.dropbox.com/sh/kx78cfpz20epnmy/AAANVKtzPsjCOdJmy6KjUvzOa?dl=0)
      (for CPU). If you want to use GPU acceleration, you can use the file [here](https://www.dropbox.com/sh/h8negvful9jhobm/AADaBgkwQ_LETg1yjemh5O9Ja?dl=0)
      <br /> <br />
      Now, just run this script in the command line (for Mac/ Linux):
```
sudo pip3 install <tensorflow_file>
```
(5) _Flask_ <br />
    
```
pip3 install Flask
```

(6) _Pre-trained checkpoint for the neural network_
    <br />
    Can be downloaded [here](https://www.dropbox.com/home/neural-guide/checkpoint)
    <br />
    **IMPORTANT** Once you downloaded the files, create create a new directory "im2txt/chk_point" and put them in there.
    