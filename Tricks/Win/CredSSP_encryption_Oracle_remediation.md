### RDP connection issue
The error occours when you try to establish an RDP connection to a target server not yet patched with the CredSSP update.

#### Method 1: regedit

Run “regedit.exe” and go to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters

There, add a DWORD value “AllowEncryptionOracle” and set it to 2.

#### Method 2: command line

Alternatively, you can launch the following from an elevated (administrator-launched) command line:

REG ADD HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters\ /v AllowEncryptionOracle /t REG_DWORD /d 2

#### Method 3: local group policy editor

Run the command “gpedit.msc”. There, go to

Local Computer Policy\Computer Configuration\Administrative Templates\System\Credentials Delegation

Double-click the line “Encryption Oracle Remediation”. Set it to Enabled with Protection Level = “Mitigated”:

 
