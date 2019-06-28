FROM python:3.6

RUN apt-get update
RUN apt-get install -y libpq-dev libxml2-dev libxmlsec1-dev libxmlsec1-openssl influxdb-client binutils libproj-dev gdal-bin

RUN pip install --upgrade pip
ENV app /canairio

RUN mkdir $app
WORKDIR $app

ADD . $app

COPY start $app/start
