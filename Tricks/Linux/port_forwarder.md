https://www.systutorials.com/port-forwarding-using-iptables/

```
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.1.2:8080
iptables -A FORWARD -p tcp -d 192.168.1.2 --dport 8080 -j ACCEPT
```
