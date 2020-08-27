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
