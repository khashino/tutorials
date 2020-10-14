### Create shortcut 
"C:\Windows\System32\cmd.exe" /k powershell.exe -windowstyle hidden -file C:\Users\khashayar\Desktop\Ftpuse.ps1

### copy to startup
1 - cntrl + R
2 - shell:startup
```
Example:
C:\Users\khashayar\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
### ftpuse.ps1
```
$fileExe = 'C:\Program Files\Ferro Software\FtpUse\'

$timer = New-Object Timers.Timer
# Set-ExecutionPolicy RemoteSigned
# Set-ExecutionPolicy Restricted
while(1)
{
#connect
If (!(Test-Path X:))
{
     Write-Host "The X: drive is already Not in use."
     Write-Host "Runing : FTPUSE"
     cd  $fileExe
     pwd
     .\ftpuse.exe X: 172.24.219.21 /HIDE

}else 
{
     Write-Host "The X: drive is already in use." 
     #cd  $fileExe
     #pwd
     #.\ftpuse.exe X: /DELETE
}
start-sleep -seconds 600

}
```
