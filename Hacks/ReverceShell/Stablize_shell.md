### 1
```
python -c 'import pty; pty.spawn(\"/bin/bash\")'
export TERM=xterm
```
Press (ctrl+Z)
```
stty raw -echo
fg
```
