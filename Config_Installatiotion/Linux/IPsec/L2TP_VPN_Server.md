https://www.tecmint.com/create-own-ipsec-vpn-server-in-linux/

### Prerequisites:

    A fresh CentOS/RHEL or Ubuntu/Debian VPS (Virtual Private Server) from any provider such as Linode.

# Setting Up IPsec/L2TP VPN Server in Linux

To set up the VPN server, we will use a wonderful collection of shell scripts created by Lin Song, that installs Libreswan as the IPsec server, and xl2tpd as the L2TP provider. The offering also includes scripts to add or delete VPN users, upgrade the VPN installation and much more.

First, log into your VPS via SSH, then run the appropriate commands for your distribution to set up the VPN server. By default, the script will generate random VPN credentials (pre-shared key, VPN username, and password) for you and display them at the end of the installation.

However, if you want to use your own credentials, first you need to generate a strong password and PSK as shown.

```
 openssl rand -base64 10
 openssl rand -base64 16
```

Next, set these generated values as described in the following command all values MUST be placed inside ‘single quotes‘ as shown.

    VPN_IPSEC_PSK – Your IPsec pre-shared key.
    VPN_USER – Your VPN username.
    VPN_PASSWORD – Your VPN password.
```
---------------- On CentOS/RHEL ---------------- 
# wget https://git.io/vpnsetup-centos -O vpnsetup.sh && VPN_IPSEC_PSK='KvLjedUkNzo5gBH72SqkOA==' VPN_USER='tecmint' VPN_PASSWORD='8DbDiPpGbcr4wQ==' sh vpnsetup.sh

---------------- On Debian and Ubuntu ----------------
# wget https://git.io/vpnsetup -O vpnsetup.sh && VPN_IPSEC_PSK='KvLjedUkNzo5gBH72SqkOA==' VPN_USER='tecmint' VPN_PASSWORD='8DbDiPpGbcr4wQ==' sudo sh vpnsetup.sh
```
The main packages that will be installed are bind-utils, net-tools, bison, flex, gcc, libcap-ng-devel, libcurl-devel, libselinux-devel, nspr-devel, nss-devel, pam-devel, xl2tpd, iptables-services, systemd-devel, fipscheck-devel, libevent-devel, and fail2ban(to protect SSH), and their respective dependencies. Then it downloads, compiles and installs Libreswan from source, enables and starts the necessary services.

### To create a new VPN user or update an existing VPN user with a new password, download and use the add_vpn_user.sh script using the following wget command.
```
wget -O add_vpn_user.sh https://raw.githubusercontent.com/hwdsl2/setup-ipsec-vpn/master/extras/add_vpn_user.sh
sudo sh add_vpn_user.sh 'username_to_add' 'user_password'
```

### To delete a VPN user, download and use the del_vpn_user.sh script.
```
wget -O del_vpn_user.sh https://raw.githubusercontent.com/hwdsl2/setup-ipsec-vpn/master/extras/del_vpn_user.sh
sudo sh del_vpn_user.sh 'username_to_delete'
```
### How to Upgrade Libreswan Installation in Linux

You can upgrade the Libreswan installation using the vpnupgrade.sh or vpnupgrade_centos.sh script. Make sure to edit the SWAN_VER variable to the version you want to install, within the script.
```
---------------- On CentOS/RHEL ---------------- 
# wget https://git.io/vpnupgrade-centos -O vpnupgrade.sh && sh vpnupgrade.sh

---------------- On Debian and Ubuntu ----------------
# wget https://git.io/vpnupgrade -O vpnupgrade.sh && sudo sh  vpnupgrade.sh
```
