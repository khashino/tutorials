```
https://ralph.blog.imixs.com/2020/02/28/howto-install-ceph-on-centos-7/

$ useradd -m cephuser -s /bin/bash
$ passwd cephuser
$ echo "cephuser ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/cephuser
$ sudo chmod 0440 /etc/sudoers.d/cephuser

# login with your cluster user
$ su cephuser
$ ssh-keygen


sudo nano /etc/hosts

192.168.137.161	ceph01
192.168.137.162	ceph02
192.168.137.163	ceph03
192.168.137.164	ceph04

$ ssh-copy-id cephuser@ceph02
$ ssh-copy-id cephuser@ceph03
$ ssh-copy-id cephuser@ceph04



ceph-deploy new ceph02 ceph03 ceph04

ceph-deploy install --release nautilus ceph02 ceph03 ceph04

ceph-deploy admin ceph02 ceph03 ceph04

ceph-deploy mgr create ceph02


ceph-deploy mds create ceph02 ceph03 ceph04

sudo ceph status 


ceph-deploy disk list ceph02



ceph-deploy osd create --data /dev/sdb ceph02
ceph-deploy osd create --data /dev/sdb ceph03
ceph-deploy osd create --data /dev/sdb ceph04



sudo ceph dashboard ac-user-create bonyan Bonyan123 administrator


https://blog.risingstack.com/ceph-storage-deployment-vm/







https://docs.ceph.com/en/nautilus/start/quick-rgw/

http://192.168.137.163:7480/

$ ceph-deploy mds create ceph02 ceph03 ceph04




Block

https://kifarunix.com/install-and-configure-ceph-block-device-on-ubuntu-18-04/
```
