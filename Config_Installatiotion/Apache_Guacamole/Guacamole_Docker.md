http://guacamole.apache.org/

https://github.com/oznu/docker-guacamole

https://hub.docker.com/r/oznu/guacamole/


```
docker run \
  -p 8080:8080 \
  -v /guacamole:/config \
  oznu/guacamole
```
```
docker run  -d --name guacamole -p 8080:8080   oznu/guacamole:armhf
```
```
Address : localhost:8080
User : guacadmin
Pass : guacadmin
```

