FROM python:3-slim

WORKDIR /home/clowder

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY csvheaders.py extractor_info.json ./

CMD python3 csvheaders.py
