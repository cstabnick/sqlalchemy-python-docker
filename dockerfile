FROM alpine as install
run apk add python3 
run apk add py3-pip
run apk add py3-psycopg2
run apk add py3-sqlalchemy


from install as base 
COPY ./app /app
workdir /app
cmd python3 main.py
