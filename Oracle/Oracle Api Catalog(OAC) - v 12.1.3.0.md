# Oracle Api Catalog(OAC) - v 12.1.3.0

## Installation

#### create user
```
useradd OAC
passwd OAC
usermod -G oinstall OAC
```
#### download these files from https://edelivery.oracle.com
```
Oracle Fusion middleware infrastructure - 12.1.3.0
Oracle Fusion middleware wls(weblogic server) - 12.1.3.0
Oracle API Catalog - 12.1.3.0
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
java -jar fmw_12.1.3.0_infrastructure.jar
```
just set Oracle home in step 2 for example </app/oac> and next next .... :D

#### Install Oracle Fusion middleware wls(weblogic)
```
unzip VXXXX_X.zip
```
You must have GUI or run it in -silence mode
```
java -jar fmw_12.1.3.0_infrastructure.jar
```
then follow steps
```
1- welcome : nothing
2- Auto update : skip auto updates
3- installation location : set oracle home same as infrastructure </app/oac>
4- installation type : Weblogic Server
5- prerequisite check : if passed next
6- installation summary : Install
7- installation progress : Finish
```
#### Install Oracle Api Catalog

https://docs.oracle.com/middleware/1213/oac/CATIG/install_cluster.htm#CATIG245

```
unzip VXXXX_X.zip
```
You must have GUI or run it in -silence mode
```
java -jar fmw_12.1.3.0.0_oac.jar
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
5- schema password : give it a password
6- customize Variable : Next
7- map tablespace : Next
8- Summary : Create
9- complete summary : Close
```
#### config domain

run Config to create domain
```
cd $ORACLE_HOME/oracle_common/common/bin
./config.sh
```
follow steps
```
1- Create domain : Create new domain - dont change the path but u can change base_domain to anything
2- Template : make sure "Create Domain Using Product Templates" is selected
  then select the following templates:
  (x)Oracle Service Bus - 12.2.1.0 [osb]
    Selecting this template automatically selects the following as dependencies:
    WebLogic Advanced Web Services for JAX-RPC Extension
    ODSI XQuery 2004 Components
    Oracle Enterprise Manager
    Oracle WSM Policy Manager
    Oracle JRF
    WebLogic Coherence Cluster Extension
  (x)Insight Service Bus Agent - 12.2.1.0 [osb] if you want to include an Oracle Real-Time Integration Business Insight agentt with Oracle Service Bus.
3- Aplication Location : Next
4- Administrator Acount : name=weblogic pass=XXXX
5- Domain mode and jdk : next
6- DB connection : connect it to databace that U install RCU - schema owner=<prefix>_STB "OSB1_STB"
7- Component Datasource : fill then next
8- JDBC Test : if passed next
9- next
10- next
11- next
12- finish
```
start the server
```
cd DOMAIN_HOME/bin
nohup ./startNodeManager.sh > LOG_DIR/nm.out&
./startWebLogic.sh
```
then open 

http://administration_server_host:administration_server_port/em
