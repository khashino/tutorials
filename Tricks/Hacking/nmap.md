# 1-scan alive 

#ping entire network
nmap -sP 192.168.137.0/24

#scanning-methodology
http://certifiedethicalhackerceh.blogspot.com/2019/07/scanning-methodology.html



# 2- scan open ports
```
nmap -sT -p 80,443 192.168.137.0/24
-sT = TCP Connect (full open scan) = 3way handshake
```
tcp udp meme
```
	1-syn = are u there
	2-syn/ack = im there lets talk
	3-ack = ok lets talk
```
## ----------
```
nmap -sS -p 80,443 192.168.137.0/24
-sS = stealthy = یواشکی (half-open)(syn scan)

	1-syn = are u there
	2-syn/ack = im there lets talk
	3-rst = never mind
```
## -----------
```
nmap -O 192.168.137.100
-O = os detection
```
## ------------
```
nmap -A 192.168.137.100
-A = os detection,script,traceroute,...
```
## ------------
```
nmap -sS -D 192.168.137.111 192.168.137.100
-D = decoy =طعمه ها = change my ip in packet
```
## ------------
```
sudo nmap --script vuln 192.168.137.100
```

## -------How start hacking-------
```
https://tryhackme.com/
https://www.hackthebox.eu/
https://www.vulnhub.com/
```



----------------------------------

#### nmap

Fully scan and ...
```
nmap -vv -sV -sC -oN <output> <IP>
```
Vuln Script
```
nmap -sV -vv --script vuln <TARGET_IP>
```
ping-sweep(only see up ip(s))
```
nmap -sn 192.168.1.0/24
```
very basic scan :| (T4 is (veryfast) speed)
```
nmap -T4 <IP>
```
scan All port full speed(-A = all detection ,-O = os detection / -T4 = Speed / -p- = all ports  ) take long time
```
nmap -T4 -A -p- <IP>
nmap -T4 -A -p22,80,514,443,111,53 <IP>
```
nmap scripts path :
```
/usr/share/nmap/scripts
/usr/local/share/nmap/scripts
```
sample use script in nmap:
```
nmap -p 443 --script=all
nmap -p 443 --script=ssl-enum-ciphers <ip/url>
```
https://github.com/nmap/nmap

