FROM debian:bookworm-slim as install
RUN apt update 
RUN apt install git bash build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev \
    xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
    -y
RUN curl https://pyenv.run | bash
RUN /root/.pyenv/bin/pyenv install 3.11.7

FROM install as pip
RUN 

FROM install as base 
COPY ./app /app
WORKDIR /app
CMD /root/.pyenv/versions/3.11.7/bin/python3 main.py
