docker container rm sqlalchemy-python-docker-psql-1
docker volume rm db-data
docker build . -t dev
docker compose up
