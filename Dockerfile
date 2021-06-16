FROM python:3.8.10-slim

RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

COPY . /checkinbox

WORKDIR /checkinbox

RUN python3 -m pip install -r requirements.txt
