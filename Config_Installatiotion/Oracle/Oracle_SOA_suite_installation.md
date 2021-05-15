 Oracle SOA - v 12.2.1.4

## Installation

#### create user
```
useradd wls
passwd wls
usermod -G oinstall wls
```
#### download these files from https://edelivery.oracle.com
```
Oracle Fusion middleware infrastructure - 12.2.1.4
Oracle Fusion middleware wls(weblogic server) - 12.2.1.4
Oracle SOA - 12.2.1.4
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
#### Installing SOA

```
 unzip V983383-01.zip
java -jar fmw_12.2.1.4.0_soa.jar
```
RCU
```
cd ORACLE_HOME/oracle_common/bin
./rcu

---check there stuff :D
User Messaging Service
Metadata Services
WebLogic Services
Oracle Platform Security Services
Audit Services
Audit Services Append
Audit Services Viewer

```

Configuring the Domain
```
ORACLE_HOME/oracle_common/common/bin
./config.sh

--check
Oracle SOA Suite Reference Configuration [soa].

--On the Advanced Configuration screen, select:
Administration Server
 Required to properly configure the listen address of the Administration Server.
Node Manager
 Required to configure Node Manager.
Topology
 Required to configure the Oracle SOA Suite Managed Server.


--Creating a New Oracle SOA Suite Machine

next next create ...

```

Starting the Servers

```
nohup ./startNodeManager.sh > LOG_DIR/nm.out&

cd DOMAIN_HOME/bin
./startWebLogic.sh

```
http://<IP>:7001/console
