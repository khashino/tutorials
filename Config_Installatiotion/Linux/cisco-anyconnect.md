https://lowendbox.com/blog/install-openconnect-server-on-ubuntu-16-04/

### Installing OCServ on Ubuntu 16.04
```
sudo apt-get update
sudo apt-get install ocserv
sudo apt-get install gnutls-bin
```
### Creating Certificates
```
cd /etc/ocserv
sudo vi ca.tmpl
```
copy
```
cn = “VPN CA”
organization = “Low End Box”
serial = 1
expiration_days = 3650
ca
signing_key
cert_signing_key
crl_signing_key
```
```
sudo certtool –generate-privkey –outfile ca-key.pem
or
certtool --generate-privkey > ca-key.pem

sudo certtool –generate-self-signed –load-privkey ca-key.pem \
–template ca.tmpl –outfile ca-cert.pem
or
certtool --generate-self-signed --load-privkey ca-key.pem    --outfile ca-cert.pem

sudo vi server.tmpl
```
copy 
```
cn = “104.236.38.188”
organization = “Low End Box”
expiration_days = 3650
signing_key
encryption_key
tls_www_server
```
```
sudo certtool –generate-privkey –outfile server-key.pem



sudo certtool –generate-certificate –load-privkey server-key.pem \
–load-ca-certificate ca-cert.pem –load-ca-privkey ca-key.pem \
–template server.tmpl –outfile server-cert.pem
or
certtool --generate-certificate --load-privkey server-key.pem    --outfile server-cert.pem --load-ca-certificate ca-cert.pem    --load-ca-privkey ca-key.pem --template server.tmpl

```
### Modify OCServ Configuration File

```
sudo vim ocserv.conf

----
Find the line auth = “pam[gid-min=1000]” and replace it with the following
auth = “plain[/etc/ocserv/ocpasswd]”

Replace these two lines
server-cert = /etc/ssl/certs/ssl-cert-snakeoil.pem
server-key = /etc/ssl/private/ssl-cert-snakeoil.key
with the following lines
server-cert = /etc/ocserv/server-cert.pem
server-key = /etc/ocserv/server-key.pem

Change the value of
try-mtu-discovery from false to true
try-mtu-discovery = true

Change the DNS value from 192.168.1.2 to 8.8.8.8
dns = 8.8.8.8

Remove the lines or place a # in front of following lines
route = 10.10.10.0/255.255.255.0
route = 192.168.0.0/255.255.0.0
no-route = 192.168.5.0/255.255.255.0
----
```
### Create Password Open Connect Server

```
sudo ocpasswd -c /etc/ocserv/ocpasswd user
```
```
sudo vim /etc/sysctl.conf
---
Uncomment the line by deleting the # from #net.ipv4.ip_forward=1.

It should look like below
net.ipv4.ip_forward=1
---
sudo sysctl -p
```
### IPTable Configuration
```
sudo iptables -A INPUT -p tcp –dport 443 -j ACCEPT
sudo iptables -A INPUT -p udp –dport 443 -j ACCEPT

#Enable NAT by using the following command
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
```
```
sudo systemctl stop ocserv.socket
sudo ocserv -c /etc/ocserv/ocserv.conf
sudo netstat -tulpn | grep 443
```


