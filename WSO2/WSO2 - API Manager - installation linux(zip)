# Installation
#### download and install oracle java jdk 8

link : https://www.oracle.com/java/technologies/javase-jdk8-downloads.html install it

rpm -ivh jdk8.rpm

check it

java -version

#### download WSO2 api manager zip file

unzip it in the path you want to install it
```
unzip wso2am-x.x.x.zip
```
#### set variables
```
export JAVA_HOME=<JDK-PATH>
export PATH=PATH=${JAVA_HOME}/bin:${PATH}
export CARBON_HOME=/.../wso2/wso2am-x.x.x(PATH OF UNZIP FILE)
```
#### change localhost to your server ip
```
cd /.../wso2/repository/conf
```
replace these files localhost to your ip :
```
api-manager.xml
carbon.xml
deployment.toml
```
#### change user and pas if u wand
defaults:
```
user: admin
pass: admin
```
You can change it in :
```
/.../wso2/repository/conf/user-mgt.xml
```
#### Start service
to start run :
```
sh /.../wso2/bin/wso2server.sh
```
or without output
```
sh /.../wso2/bin/wso2server.sh start
sh /.../wso2/bin/wso2server.sh stop
```
### Open it With Ur Browser
```
https://<hostname>:9443/publisher
```
