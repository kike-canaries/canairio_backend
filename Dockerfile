FROM python:3.6

RUN apt-get update
RUN apt-get install -y libpq-dev libxml2-dev libxmlsec1-dev libxmlsec1-openssl

ENV app /canairio

RUN mkdir $app
WORKDIR $app

ADD . $app
RUN pip install -r requirements.txt
RUN python manage.py migrate
