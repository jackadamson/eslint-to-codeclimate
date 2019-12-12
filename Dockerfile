FROM python:3.6-alpine
WORKDIR /working
ADD convertresults.py /usr/local/bin/convertresults

CMD convertresults
