## config sftp user only without ssh 

### first step
create user and group
```
groupadd sftpusers
useradd -g sftpusers -s /sbin/nologin ftpuser
passwd ftpuser
```

### edit sshd_config

nano /etc/ssh/sshd_config

replace this
```
#Subsystem      sftp    /usr/libexec/openssh/sftp-server
Subsystem       sftp    internal-sftp
```
add these line at the end of file
```
Match Group sftpusers
X11Forwarding no
AllowTcpForwarding no
ChrootDirectory %h
ForceCommand internal-sftp

Match User ftpuser
  ChrootDirectory /home/ftpuser/
  ForceCommand internal-sftp
  AllowTcpForwarding no
  X11Forwarding no
```
### reset service
```
systemctl restart sshd.service
```
### set file owner

change owner too root and ...

```
chown -R root /home/ftpuser
chmod -R 755 /home/ftpuser
chown ftpuser /home/ftpuser/data
```
