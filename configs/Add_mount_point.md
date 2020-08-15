```
fdisk -l | grep -i dev
```
//example:new disk is /dev/sdb   
```
pvcreate /dev/sdb              
```
```
vgcreate vgapp /dev/sdb
```
```
lvcreate --name lvapp --size 200G vgapp
```
```
mkfs.ext4 /dev/mapper/vgapp-lvapp
```
```
mkdir /app
mount /dev/mapper/vgapp-lvapp /app
```
```
vi /etc/fstab
/dev/mapper/vgapp-lvapp  /app   ext4   defaults   0 0
```
