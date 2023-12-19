FROM alpine as deps
run apk add python3 
run apk add py3-pip

from deps as install
COPY ./setup /setup
workdir /setup
run pip install -r /setup/requirements.txt

from install as base 
COPY ./app /app
workdir /app
cmd python3 main.py
