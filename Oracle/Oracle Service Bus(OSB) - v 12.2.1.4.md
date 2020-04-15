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

#### Install Oracle Fusion middleware wls(weblogic)
```
unzip VXXXX_X.zip
```
You must have GUI or run it in -silence mode
```
java -jar fmw_12.2.1.4.0_infrastructure.jar
```
then follow steps
```
1- welcome : nothing
2- Auto update : skip auto updates
3- installation location : set oracle home same as infrastructure </app/osb>
4- installation type : Weblogic Server
5- prerequisite check : if passed next
6- installation summary : Install
7- installation progress : Finish
```
#### Install Oracle Service Bus
```
unzip VXXXX_X.zip
```
You must have GUI or run it in -silence mode
```
java -jar fmw_12.2.1.4.0_osb.jar
```
then follow steps
```
1- welcome : nothing
2- Auto update : skip auto updates
3- installation location : set oracle home same as infrastructure </app/osb>
4- installation type : Service Bus
5- prerequisite check : if passed next
6- installation summary : Install
7- installation progress : Finish
```

## Configure Domain

Oracle Tutorial : https://docs.oracle.com/middleware/1221/core/INOSB/GUID-36DFF16B-4891-46EB-9554-436A3CCF85BB.htm#INSOA380

#### RCU
first U must have Database . then run RCU to create repository utilities
```
cd $ORACLE_HOME/oracle_common/bin
./rcu
```
follow steps
```
1- welcome : next
2- create repository : check System load and product load
3- db connection : 
  For example:
    Database Type: Oracle Database
    Name: examplehost.exampledomain.com
    Port: 1521
    Service Name: Orcl.exampledomain.com
    User Name: sys
    Password: ******
    Role: SYSDBA
4- select component : select Create new prefix and give it a name like "OSB1"
   then just select "SOA Suite" it will select other automaticly 
   then next
5-   
