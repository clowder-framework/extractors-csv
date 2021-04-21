FROM python:3-slim

WORKDIR /home/clowder
COPY csvheaders.py extractor_info.json /home/clowder

COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD python3 csvheaders.py
