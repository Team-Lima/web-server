# get base image
FROM congying/docker-ubuntu-python-opencv:latest

#install python and pip
RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get -y install python3 python3-pip

COPY requirements.txt /usr/src/NeuralGuideServer/
RUN pip3 install --no-cache-dir -r /usr/src/NeuralGuideServer/requirements.txt

COPY server.py /usr/src/NeuralGuideServer/
COPY image.py /usr/src/NeuralGuideServer/
COPY auth.py /usr/src/NeuralGuideServer/
COPY config.py /usr/src/NeuralGuideServer/
COPY exceptions.py /usr/src/NeuralGuideServer/
COPY run_from_disk.py /usr/src/NeuralGuideServer/
COPY server_util_functions.py /usr/src/NeuralGuideServer/

COPY image_processor /usr/src/NeuralGuideServer/image_processor
COPY im2txt /usr/src/NeuralGuideServer/im2txt

RUN mkdir /usr/src/NeuralGuideServer/im2txt/chk_point/
RUN cd /usr/src/NeuralGuideServer/im2txt/chk_point/
RUN wget -O graph.pbtxt https://dl.dropboxusercontent.com/s/u84fgiorxn1zlqe/graph.pbtxt?dl=0
RUN wget -O model.ckpt-2000000 https://dl.dropboxusercontent.com/s/okbsfriqi2p03s4/model.ckpt-2000000?dl=0
RUN wget -O model.ckpt-2000000.meta https://dl.dropboxusercontent.com/s/l9sboeglrg2bv0w/model.ckpt-2000000.meta?dl=0 

EXPOSE 5000

CMD ["python3", "/usr/src/NeuralGuideServer/server.py"]
