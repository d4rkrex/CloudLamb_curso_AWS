FROM python:3.8-slim-buster

LABEL maintainer="manuel.roldan@naranjax.com"
LABEL version="1.0"
LABEL description="retrive public IPs from Nx AWS accounts"

RUN apt-get update -y && \
 		apt-get install -y build-essential curl git

RUN git clone https://github.com/golismero/openvas_lib.git && cd openvas_lib && python3 setup.py install

ADD ./app /vas-bff

WORKDIR /vas-bff

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD [ "python3", "api.py"]