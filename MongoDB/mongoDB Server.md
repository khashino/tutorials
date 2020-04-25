# MongoDB Server Installation 
https://www.thepolyglotdeveloper.com/2019/01/getting-started-mongodb-docker-container-deployment/

you can install it with DOCKER this is the easiest way
```
docker pull mongo
docker pull mongo:4.0.4
docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4
docker exec -it mongodb bash
```
## Use Mongo with command line
```
mongo #connect to mongo
show dbs  #show Databases
use mydb  #Use Database
show collections  #show collections(tables)
```
### some examples
```
db.people.save({ firstname: "Nic", lastname: "Raboy" })
db.people.find({ firstname: "Nic" })
db.people.find()
db.people.find().pretty()
```

### Some Features
(x)-Materialized view
(x)-sharding
(x)-Replication
...
