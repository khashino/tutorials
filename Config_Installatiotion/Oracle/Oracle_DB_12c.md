## How to Install Oracle Database 12c on CentOS 7
#### Step 1 - Install required Packages
```
yum install -y binutils.x86_64 compat-libcap1.x86_64 gcc.x86_64 gcc-c++.x86_64 glibc.i686 glibc.x86_64 \
glibc-devel.i686 glibc-devel.x86_64 ksh compat-libstdc++-33 libaio.i686 libaio.x86_64 libaio-devel.i686 libaio-devel.x86_64 \
libgcc.i686 libgcc.x86_64 libstdc++.i686 libstdc++.x86_64 libstdc++-devel.i686 libstdc++-devel.x86_64 libXi.i686 libXi.x86_64 \
libXtst.i686 libXtst.x86_64 make.x86_64 sysstat.x86_64
```
#### Step 2 - Configure User and System
```
groupadd oinstall
groupadd dba
useradd -g oinstall -G dba oracle
passwd oracle
TYPE THE PASSWORD
```
Edit 'sysctl.conf' file with vim.
```
vim /etc/sysctl.conf
```
Paste configuration below.
```
fs.aio-max-nr = 1048576
fs.file-max = 6815744
kernel.shmall = 2097152
kernel.shmmax = 2147483648
kernel.shmmni = 4096
kernel.sem = 250 32000 100 128
net.ipv4.ip_local_port_range = 9000 65500
net.core.rmem_default = 262144
net.core.rmem_max = 4194304
net.core.wmem_default = 262144
net.core.wmem_max = 1048586
```
Now run the commands below to display all kernel parameter and apply the new values.
```
sysctl -p
sysctl -a
```
edit 'limits.conf' file with vim.
```
vim /etc/security/limits.conf
```
Paste the configuration below.
```
oracle soft nproc 2047
oracle hard nproc 16384
oracle soft nofile 1024
oracle hard nofile 65536
```
#### Step 3 - Configure Desktop
1- download 12c for Linux.
```
yum -y install zip unzip
```
unzip downloaded file to a new directory named 'stage'.
```
unzip linuxamd64_12102_database_se2_1of2.zip -d /stage/
unzip linuxamd64_12102_database_se2_2of2.zip -d /stage/
```
Change owner and group of the '/stage/' directory to the oracle user and oinstall group.
```
chown -R oracle:oinstall /stage/
```
```
mkdir -p /u01 /u02
chown -R oracle:oinstall /u01 /u02
chmod -R 775 /u01 /u02
chmod g+s /u01 /u02
```
#### Step 5 - Install Oracle Database 12c
```
ssh -X oracle@192.168.33.15
cd /stage/database/
./runInstaller
```
```
1- Next
2- At 'Installation Options', choose 'Create and configure a database' and click 'Next'.
3- Under the 'System Class' section, choose 'Desktop Class' and click 'Next' again.
4- 'Typical Installation' info.
    Oracle base: '/u01/app/oracle'
    Software location: /u01/app/oracle/product/12.1.0/dbhome_1
    Database file location: /u02
    Database edition: Default
    Character set: Default
    OSDBA group: dba
    Global database name: Type your own name
    Administrative password: Type your own password
    Confirm password: Type again
    Uncheck the 'Create as Container database'
    Click Next.
5- At 'Create Inventory', enter the path below:
    Inventory Directory: /u01/app/oraInventory
    oraInventory Group Name: use 'oinstall' group.
    Click 'Next'.
6- Click 'Install'.
7- Open a new terminal and execute the files.
    ssh root@192.168.33.15
    /u01/app/oraInventory/orainstRoot.sh
    /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
```
#### Step 6 - Testing
Log in to the server and access the oracle user.
```
ssh root@192.168.33.15
TYPE YOUR PASSWORD
```
Login to the oracle user.
```
su - oracle
```
Execute the commands below to set the oracle environment.
```
export ORACLE_SID=orcl
export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1/
export PATH=$PATH:$ORACLE_HOME/bin
```
Access the oracle database utility 'sqlplus', log in as 'sysdba' privileges.
```
sqlplus / as sysdba
```
Oracle comes with some default users. Run the query below if you want to change the default user named 'sys'.
```
alter user sys identified by yourpassword;
```

#### Oracle Enterprise Manager
https://localhost:5500/em/
