# Hack Tools

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

https://github.com/OJ/gobuster

#### nmap

port scan and ...
```
nmap -vv -sV -sC -oN <output> <IP>
```

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

#### nmap
Important !!! :D

https://github.com/nmap/nmap
```
nmap -p <port> <range>
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
