FROM python:3

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

COPY . .
RUN python setup.py install
