runs postgres and a python script with sqlalchemy as docker containers

requires `docker` 

to run execute the file run.sh
`sh run.sh`
this rebuilds the docker container containing the python script in app/ and prints out an example record

this will create one volume and two container 
review these with 

`docker container ls`

`docker volume ls`
