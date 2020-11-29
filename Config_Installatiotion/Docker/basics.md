### save/load
```
docker save -o ./apache_nifi.tar apache/nifi
docker load -i ./apache_nifi.tar
```
### install from binary
docker
```
https://docs.docker.com/engine/install/binaries/
```
docker-compose
```
https://docs.docker.com/compose/install/
```

### SSH into a Container
```
docker ps
docker exec -it <container name> /bin/bash
```

### clustering
Docker Swarm

