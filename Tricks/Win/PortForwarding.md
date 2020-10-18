
# Add 
```
netsh interface portproxy add v4tov4 listenaddress=localaddress listenport=localport connectaddress=destaddress connectport=destport
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=9000 connectaddress=192.168.0.10 connectport=80

```
# Del
```
netsh interface portproxy delete v4tov4 listenaddress=127.0.0.1 listenport=9000
netsh interface portproxy reset
```
# other
```
netstat -na|find "3340"
Test-NetConnection -ComputerName localhost -Port 3340
netstat -ano | findstr :3340
```
You can find out what process is listening on the specified port using its PID (in our example, the PID is 636):
```
tasklist | findstr 636
```
# firewall
```
netsh advfirewall firewall add rule name=”forwarded_RDPport_3340” protocol=TCP dir=in localip=10.1.1.110  localport=3340 action=allow
```
Or using the New-NetFirewallRule PowerShell cmdlet:
```
New-NetFirewallRule -DisplayName "forwarder_RDP_3340" -Direction Inbound -Protocol TCP –LocalPort 3340 -Action Allow
```
To display a list of all active TCP port forwarding rules on Windows, run the command:
```
netsh interface portproxy show all
```
You can also list port forwarding settings in portproxy as follows:
```
netsh interface portproxy dump
```
