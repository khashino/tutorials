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

