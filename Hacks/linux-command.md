# useful linux command
Getting Data from Web Servers nc
```
echo -en "GET / HTTP/1.0\n\n\n" | netcat www.linode.com 80
```
Using netcat for Transferring Files
```
cat access.log | nc -vv -l -p 4567
nc -vv localhost 4567 > fileToGet
```
nc port scan
```
netcat -z -vv -n 127.0.0.1 1-30
nc -z -v -n 127.0.0.1 1-30
```
nc Private chat
```
mawk -W interactive '$0="Alice: "$0' | nc -l -p <port_number> <ip_of_alice>
mawk -W interactive '$0="Bob: "$0' | nc <ip_of_alice> <port_number>
```
add text to first of file
```
perl -pi -e 'print "***" if $.==1' file
```
show disk usage
```
du -sh
```
show disks
```
df -ah
```
show open ports
```
netstat -tulpn
```
show CPU stuff
```
ps aux | grep nginx
top
htop
```
mount cmnds
```
ls /mnt
mount <1> <2>
```
disk and files
```
less /etc/fstab
```
sed
```
sed '1,2d;$1d'
sed 's/[^0-9]*//g' #export numbers
```
solaris check patchnum
```
showver -p
pkginfo | grep <SUN****>
pkgparam -v <****>
```
sum list of numbers
```
awk '{sum += $1} End { Print sum }'
```
make sounds
```
say <****>
msay <****>
espeak <****>
beep #motherboard sound
```
Copy with bar
```
rsync -avz -process <1> <2>
rsync -ah <1> <2>
gcp -pv <1> <2>
```
