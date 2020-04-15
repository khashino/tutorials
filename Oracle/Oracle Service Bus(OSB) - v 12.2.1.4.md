# Oracle Service Bus(OSB) - v 12.2.1.4

## Installation

#### create user
```
useradd osb
passwd osb
usermod -G oinstall osb
```
#### download these files from https://edelivery.oracle.com
```
Oracle Fusion middleware infrastructure - 12.2.1.4
Oracle Fusion middleware wls(weblogic server) - 12.2.1.4
Oracle Service Bus - 12.2.1.4
```
#### download and install oracle java jdk 8
link : https://www.oracle.com/java/technologies/javase-jdk8-downloads.html
install it 
```
rpm -ivh jdk8.rpm
```
check it
```
java -version
```
set JAVA_HOME,PATH
```
export JAVA_HOME="<JDK-PATH>"
echo $JAVA_HOME
export PATH="$PATH:<JDK-PATH>"
exho $PATH
```

#### Install Oracle Fusion middleware infrastructure
```
unzip VXXXX_X.zip
```
You must have GUI or run it in -silence mode
```
java -jar fmw_12.2.1.4.0_infrastructure.jar
```
just set Oracle home in step 2 for example </app/osb> and next next .... :D


