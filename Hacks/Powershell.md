#### Speak
```
Add-Type -AssemblyName System.speech
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speak.Speak('Hello...')
```
```
$speak.Rate = -10
$speak.Speak("The current date and time is $(Get-Date)")
```
#### Sound
```
[System.Console]::Beep()
[console]::beep(1000,500)
[system.media.systemsounds]::Beep.play()
[system.media.systemsounds]::Asterisk.play()
[system.media.systemsounds]::Exclamation.play()
[system.media.systemsounds]::Hand.play()
```
#### Kill a process
```
get-process BadTh*
stop-process -id 2792
```
#### Minimize all windows
```
$shell = New-Object -ComObject "Shell.Application"
$shell.minimizeall()
```
undo:
```
$shell = New-Object -ComObject "Shell.Application"
$shell.undominimizeall()
```
#### run powershell cmd hidden
```
PowerShell.exe -windowstyle hidden <CMD>
```
#### send message
```
msg <*/user> <msg>
```
#### get user pass
```
Get-Credential
Get-Credential -UserName domain\user -Message 'Enter Password'
```
```
$Credentials = Get-Credential
$Credentials.Password | ConvertFrom-SecureString | Set-Content C:\test\password.txt
$Username = $Credentials.Username
$Password = Get-Content “C:\test\password.txt”
```
#### pop up
```
Add-Type -AssemblyName PresentationCore,PresentationFramework
$ButtonType = [System.Windows.MessageBoxButton]::YesNo
$MessageboxTitle = “Test pop-up message title”
$Messageboxbody = “Are you sure you want to stop this script execution?”
$MessageIcon = [System.Windows.MessageBoxImage]::Warning
[System.Windows.MessageBox]::Show($Messageboxbody,$MessageboxTitle,$ButtonType,$messageicon)
```
```
Add-Type -AssemblyName PresentationCore,PresentationFramework
$ButtonType = [System.Windows.MessageBoxButton]::YesNoCancel
$MessageIcon = [System.Windows.MessageBoxImage]::Error
$MessageBody = "Are you sure you want to delete the log file?"
$MessageTitle = "Confirm Deletion"
 
$Result = [System.Windows.MessageBox]::Show($MessageBody,$MessageTitle,$ButtonType,$MessageIcon)
 
Write-Host "Your choice is $Result"
```
#### Create Box
```
[void][System.Reflection.Assembly]::LoadWithPartialName("System.Drawing")
 
[void][System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
 
$objForm = New-Object System.Windows.Forms.Form
 
 
 
$objForm.Text = "Login Again"
 
$objForm.Size = New-Object System.Drawing.Size(300, 250)
 
$objForm.StartPosition = "CenterScreen"
 
 
 
$objForm.KeyPreview = $True
 
 
 
$OKButton = New-Object System.Windows.Forms.Button
 
$OKButton.Location = New-Object System.Drawing.Size(75, 150)
 
$OKButton.Size = New-Object System.Drawing.Size(75, 23)
 
$OKButton.Text = "Login"
 
#$objServer_TextBox.TabIndex = 2
 
$OKButton.Add_Click({ $objForm.Close() })
 
$objForm.Controls.Add($OKButton)
 
$objForm.Add_KeyDown({
 
        if ($_.KeyCode -eq "Enter")
 
        {
           $objForm.Close()
        }
 
    })
 
 
 
$CancelButton = New-Object System.Windows.Forms.Button
 
$CancelButton.Location = New-Object System.Drawing.Size(150, 150)
 
$CancelButton.Size = New-Object System.Drawing.Size(75, 23)
 
$CancelButton.Text = "Restart"
 
#$objServer_TextBox.TabIndex = 3
 
#$CancelButton.Add_Click({ $objForm.Close() })
$CancelButton.Add_Click({ })
 
$objForm.Controls.Add($CancelButton)
 
$objForm.Add_KeyDown({
 
        if ($_.KeyCode -eq "Escape")
        { 
        }
 
    })
 
 
 
#This creates a label for the Server_TextBox
 
$objServer_Label = New-Object System.Windows.Forms.Label
 
$objServer_Label.Location = New-Object System.Drawing.Size(10, 20)
 
$objServer_Label.Size = New-Object System.Drawing.Size(280, 20)
 
$objServer_Label.Text = "Username :"
 
$objForm.Controls.Add($objServer_Label)
 
 
 
#This creates the TextBox1
 
$objServer_TextBox1 = New-Object System.Windows.Forms.TextBox
 
$objServer_TextBox1.Location = New-Object System.Drawing.Size(10, 40)
 
$objServer_TextBox1.Size = New-Object System.Drawing.Size(260, 20)
 
#$objServer_TextBox.TabIndex = 0
 
$objForm.Controls.Add($objServer_TextBox1)
 
 
 
#This creates a label for the TextBox2
 
$objService_Label2 = New-Object System.Windows.Forms.Label
 
$objService_Label2.Location = New-Object System.Drawing.Size(10, 70)
 
$objService_Label2.Size = New-Object System.Drawing.Size(280, 20)
 
$objService_Label2.Text = "Password :"
 
$objForm.Controls.Add($objService_Label2)
 
 
 
#This creates the TextBox2
 
$objService_TextBox2 = New-Object System.Windows.Forms.TextBox
 
$objService_TextBox2.Location = New-Object System.Drawing.Size(10, 90)
 
$objService_TextBox2.Size = New-Object System.Drawing.Size(260, 20)
 
#$objService_TextBox2.TabIndex = 1
 
$objForm.Controls.Add($objService_TextBox2)
 
 
 
$objForm.Topmost = $True
 
 
 
$objForm.Add_Shown({ $objForm.Activate() })
 
[void]$objForm.ShowDialog()

echo $objServer_TextBox1.text 
echo $objService_TextBox2.text 
```
```
[void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic')

$title = 'Demographics'
$msg   = 'Enter your demographics:'

$text = [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)
```
```
 [void][System.Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic')

$name = [Microsoft.VisualBasic.Interaction]::InputBox("Enter your name", "Name", "$env:username")

"Your name is $name$"
```

