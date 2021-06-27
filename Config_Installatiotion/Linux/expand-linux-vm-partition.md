https://www.netwoven.com/2018/07/10/expand-linux-vm-partition/
```
fdisk -l

fdisk /dev/sda

Partition number (1-4): 3

Hex code (type L to list codes): 8e

Command (m for help): w

Reboot the system.

pvcreate /dev/sda3

vgdisplay

vgextend VolGroup /dev/sda3

lvdisplay

lvextend /dev/VolGroup/lv_root /dev/sda3

Xfs_growfs /dev/VolGroup/lv_root

df -h
```


## Centos7
```

fdisk /dev/sdf
  To Create new partition Press n.
  Choose primary partition use p.
  Choose which number of partition to be selected to create the primary partition.
  Press 1 if any other disk available.
  Change the type using t.
  Type 8e to change the partition type to Linux LVM.
  Use p to print the create partition ( here we have not used the option).
  Press w to write the changes.
fdisk -l /dev/sdf
pvcreate /dev/sdf1
pvs
vgextend centos /dev/sdf1
vgs
pvscan
lvdisplay
vgdisplay
lvextend -l +127999 /dev/centos/root
xfs_growfs /dev/centos/root

```
