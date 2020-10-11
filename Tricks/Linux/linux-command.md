# useful linux command
diff two directory
```
diff <(ls -1a . | grep csv|sed 's/.\{3\}$//') <(ls -1a .| grep dat|sed 's/.\{3\}$//')
```
sar -r in MB
```
sar -r 1 | awk -v OFS='   ' '{if($3 ~ /^[:0-9:]/) if($1 ~ /^[:0-9:]/) {print $1,$2,$3/1024,$4/1024,$5,$6/1024,$7/1024,$8/1024,$9,$10/1024,$11/1024} if ($3 ~ /^[:a-z:]/) {print $0} if ($1 ~ /^[:A-Z:]/) {print $0}}'
```
mount smb on linux
```
mount.cifs //192.168.137.20/APPS2/ /apps/mount/APPS2 -o user=khashayar
```
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
