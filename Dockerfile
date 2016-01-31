FROM python:2.7
MAINTAINER Matthias Endler <matthias-endler@gmx.net>

COPY . /kafka-influxdb
WORKDIR /kafka-influxdb
RUN python setup.py install
CMD ["./run.sh"]
