# out base image
FROM ubuntu:16.04

#install python and pip
RUN apk add --update py3-pip

COPY requirements.txt /usr/src/NeuralGuideServer/
RUN pip3 install --no-cache-dir -r /usr/src/NeuralGuideServer/requirements.txt

RUN ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)" PATH="$HOME/.linuxbrew/bin:$PATH"
RUN echo 'export PATH="$HOME/.linuxbrew/bin:$PATH"' >>~/.bash_profile

RUN sudo apt-get install build-essential curl git python-setuptools ruby
RUN brew install opencv3 --with-python3 --with-contrib
RUN echo 'export PYTHONPATH=$PYTHONPATH:/usr/local/Cellar/opencv3/3.0.0/lib/python3.4/site-packages' >>~/.profile
RUN source ~/.profile

COPY server.py /usr/src/NeuralGuideServer/
COPY image.py /usr/src/NeuralGuideServer/
COPY auth.py /usr/src/NeuralGuideServer/
COPY config.py /usr/src/NeuralGuideServer/
COPY exceptions.py /usr/src/NeuralGuideServer/
COPY run_from_disk.py /usr/src/NeuralGuideServer/
COPY server_util_functions.py /usr/src/NeuralGuideServer/

COPY image_processor /usr/src/NeuralGuideServer/image_processor
COPY im2txt /usr/src/NeuralGuideServer/im2txt

COPY dependencies /usr/src/NeuralGuideServer/dependencies

RUN sudo pip3 install /usr/src/NeuralGuideServer/dependencies/tensorflow-0.12.0-py3-none-any.whl

EXPOSE 5000

CMD ["python", "/usr/src/NeuralGuideServer/server.py"]