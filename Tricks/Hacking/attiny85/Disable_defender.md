https://www.itechtics.com/enable-disable-windows-defender/

## How To Permanently Disable Windows Defender Using PowerShell

Run PowerShell with administrative privileges (Windows key + X + A)

To disable real-time monitoring for Windows Defender, run the following command:
```
Set-MpPreference -DisableRealtimeMonitoring $true
```
To enable real-time monitoring, run the following command:
```
Set-MpPreference -DisableRealtimeMonitoring $false
```

## How To Disable Windows Defender Using Command Prompt

### disable temprory
Open command prompt with administrative privileges
Run the following command to disable Windows Defender:
```
sc stop WinDefend
```
To enable Windows defender again, run the following command:
```
sc start WinDefend
```

### disable permanetly
```
sc config WinDefend start= disabled
sc stop WinDefend
```

To enable it again on startup, run the following commands:
```
sc config WinDefend start= auto
sc start WinDefend
```
If you want to check the current state of the Windows Defender service, run the following command:
```
sc query WinDefend
```
