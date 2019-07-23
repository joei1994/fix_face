FROM ubuntu:16.04

RUN apt-get update; \
    apt-get -y install build-essential cmake;\
    apt-get -y install libopenblas-dev liblapack-dev; \
    apt-get -y install libx11-dev libgtk-3-dev; \
    apt-get -y install python python-dev python-pip; \
    apt-get -y install python3 python3-dev python3-pip
    
COPY ./app.py /home
COPY ./requirements.txt /home
COPY ./utils.py /home

WORKDIR /home
RUN pip3 install -r requirements.txt

WORKDIR /home
CMD python3 app.py

EXPOSE 80