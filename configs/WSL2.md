#### WSL 2 
Install the Windows Subsystem for Linux
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
Update to WSL 2
(Running Windows 10, updated to version 2004, Build 19041 or higher.)
```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
Set WSL 2 as your default version
```
wsl --set-default-version 2
```
WSL 2 requires an update to its kernel component. For information please visit https://aka.ms/wsl2kernel

Install your Linux distribution of choice from microsoft store

#### list of wsl os
```
wsl -l -v
```
#### backup and restore
```
wsl --export <>.tar
wsl --import <>.tar
```
### Use GUI (RDP) for linux on wsl2
```
sudo apt install xfce4
sudo apt install xrdp
sudo /etc/init.d/xrdp start
```
### port forwarding on wsl2

add new rule in firewall for that port

then:
```
 netsh interface portproxy add v4tov4 listenport=3000 listenaddress=0.0.0.0 connectport=3000 connectaddress=172.24.227.202<wsl2 ip>
```
