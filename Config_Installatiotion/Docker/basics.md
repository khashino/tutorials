### save/load
```
docker save -o ./apache_nifi.tar apache/nifi
docker load -i ./apache_nifi.tar
```
### install from binary
#### docker
```
https://docs.docker.com/engine/install/binaries/
```

```
https://download.docker.com/linux/static/stable/
tar xzvf /path/to/<FILE>.tar.gz
sudo cp docker/* /usr/bin/
sudo dockerd &
```
#### docker-compose
```
https://docs.docker.com/compose/install/
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version
```

### SSH into a Container
```
docker ps
docker exec -it <container name> /bin/bash
```

### clustering
Docker Swarm

### Removing
Remove a container
```
docker rm /redis
```
Force-remove a running container
```
docker rm --force redis
```
Remove all stopped containers
```
docker rm $(docker ps -a -q)
```
Remove a container and its volumes
```
docker rm -v redis
```

### Stop and remove container
```
docker container ls -a
docker container ls –aq 
docker container stop [container_id]
docker container rm [container_id]
```
```
docker container stop $(docker container ls –aq)
docker container rm $(docker container ls –aq)
```
### Remove All Docker Containers
To wipe Docker clean and start from scratch
```
docker container stop $(docker container ls –aq) && docker system prune –af ––volumes
```



