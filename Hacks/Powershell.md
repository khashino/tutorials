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
 
$OKButton.Location = New-Object System.Drawing.Size(75, 250)
 
$OKButton.Size = New-Object System.Drawing.Size(75, 23)
 
$OKButton.Text = "Login"
 
#$objServer_TextBox.TabIndex = 2
 
$OKButton.Add_Click({ $xServerName = $objServer_TextBox1.Text; $xService = $objTextBox2.Text; $objForm.Close() })
 
$objForm.Controls.Add($OKButton)
 
$objForm.Add_KeyDown({
 
        if ($_.KeyCode -eq "Enter")
 
        {
 
            $script:xServerName = $objServer_TextBox1.Text; $xService = $objTextBox2.Text; $objForm.Close()
 
        }
 
    })
 
 
 
$CancelButton = New-Object System.Windows.Forms.Button
 
$CancelButton.Location = New-Object System.Drawing.Size(150, 250)
 
$CancelButton.Size = New-Object System.Drawing.Size(75, 23)
 
$CancelButton.Text = "Restart"
 
#$objServer_TextBox.TabIndex = 3
 
$CancelButton.Add_Click({ $objForm.Close() })
 
$objForm.Controls.Add($CancelButton)
 
$objForm.Add_KeyDown({
 
        if ($_.KeyCode -eq "Escape")
 
        { $objForm.Close() }
 
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

echo $objService_TextBox2
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

