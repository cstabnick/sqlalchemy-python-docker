FROM debian:bookworm-slim as install
RUN apt update 
RUN apt install git bash build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev \
    xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
    -y
RUN curl https://pyenv.run | bash
RUN /root/.pyenv/bin/pyenv install 3.11.7
RUN cp /root/.pyenv/versions/3.11.7/bin/pip /usr/bin
RUN cp /root/.pyenv/versions/3.11.7/bin/python /usr/bin

FROM install as pip 
RUN /root/.pyenv/versions/3.11.7/bin/pip install sqlalchemy fastapi
RUN pip install "uvicorn[standard]"
RUN ln -s /root/.pyenv/versions/3.11.7/bin/uvicorn /usr/bin
RUN pip install psycopg2-binary

FROM pip as base 
# expects the /app dir to be mounted in the compose file
# COPY ./app /app 
WORKDIR /app
CMD ["uvicorn",  "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
