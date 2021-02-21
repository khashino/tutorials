https://www.systutorials.com/port-forwarding-using-iptables/

```
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.1.2:8080
iptables -A FORWARD -p tcp -d 192.168.1.2 --dport 8080 -j ACCEPT
```

# 2

https://jensd.be/343/linux/forward-a-tcp-port-to-another-ip-or-port-using-nat-with-iptables

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 9999 -j DNAT --to-destination 192.168.202.105:80
sudo iptables -t nat -A POSTROUTING -p tcp -d 192.168.202.105 --dport 80 -j SNAT --to-source 192.168.202.103
sudo iptables -t nat -L -n
```
