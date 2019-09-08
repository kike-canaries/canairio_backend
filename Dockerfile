FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y libpq-dev libxml2-dev libxmlsec1-dev libxmlsec1-openssl influxdb-client binutils libproj-dev gdal-bin

RUN pip install --upgrade pip

RUN mkdir canairio/
WORKDIR canairio/
COPY requirements.txt /canairio/
RUN pip install -r requirements.txt
COPY . /canairio/
