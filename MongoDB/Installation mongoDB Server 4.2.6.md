# MongoDB Server Installation 
https://www.thepolyglotdeveloper.com/2019/01/getting-started-mongodb-docker-container-deployment/
```
docker pull mongo
docker pull mongo:4.0.4
docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4
docker exec -it mongodb bash
mongo
show dbs
use mydb
db.people.save({ firstname: "Nic", lastname: "Raboy" })
db.people.find({ firstname: "Nic" })
```
