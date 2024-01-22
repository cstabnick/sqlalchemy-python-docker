Requires `docker` 

Example docker-compose application which runs postgres and a python script with sqlalchemy.


To run, execute the file run.sh `sh run.sh`.
This rebuilds the docker container described in `dockerfile` and runs docker compose attached to the containers.

This will create one volume and two containers. Review these with: 

`docker container ls`

`docker volume ls`


This solution is intended to be used to demonstrate a potential development environment which involves the developer modifying /app, and running run.sh to start the application.
 
