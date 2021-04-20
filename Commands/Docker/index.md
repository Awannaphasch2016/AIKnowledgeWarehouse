:docker:basic:
* enter to docker interactive mode
    * `docker exec -it *ContaineID* bash`

:docker:basic:
* list docker images that are not closed yet
    * `docker -ps`

:docker:basic:
* running jupyter image on docker
    * `docker run -p local_computer_port:docker_port jupyter/scipy`

docker:basic:
* inspect path that vol is mounted to
    * `docker inspect -f '{{ .Mounts }}' *ContainerID* `

docker:basic:volume:
* list volume
    * `docker volume ls`

docker:basic:image:
* show image history
    * `docker history *Image*`

docker:basic:
* remove all container
    * `docker rm -f $(docker ps -aq)`

docker:basic:
* launch superset image
    * `docker run -d -p 8088:8088 typlerfowler/superset`

docker:basic:example:mount:volume:
* bind mount volume to container
    * `docker run -d -p 5432:5432 -v pgdata:/var/lib/postgresql/data postgres` 
