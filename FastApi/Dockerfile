FROM ubuntu:20.04 

RUN apt update && apt upgrade -y && apt install python3 -y && apt install python3-pip -y && apt install git -y && apt autoremove -y 

RUN git clone https://github.com/ioSoyPato/Data-Engineer-Project.git

WORKDIR /FastApi

RUN pip3 install -r requirements.txt

EXPOSE 4444

CMD python3 main.py 