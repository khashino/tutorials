## Offline:
https://www.programmersought.com/article/76933922577/
## Online
https://phoenixnap.com/kb/how-to-setup-ftp-server-install-vsftpd-centos-7


# OFFLINE
download vsftpd from mirror
```
http://mirror.centos.org/centos/7/os/x86_64/Packages/vsftpd-3.0.2-28.el7.x86_64.rpm
```
install it
```
 rpm -ivh vsftpd-3.0.2-27.el7.x86_64.rpm
```
config
```
cd /etc/vsftpd/
nano vsftpd.conf
systemctl start vsftpd.service
```
add user
```
cd /etc/vsftpd/
nano user_list
systemctl restart vsftpd.service
```

## errors
503 Permission denied
```
vi /etc/vsftpd/vsftpd.conf
userlist_enable=YES
userlist_deny=NO
```

500 OOPS: could not read chroot() list
```
#chroot_list_enable=YES
#chroot_list_file=/etc/vsftpd.chroot_list
```
