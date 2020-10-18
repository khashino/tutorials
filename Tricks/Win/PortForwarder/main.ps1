foreach($line in Get-Content .\file.txt) {
    $hhost,$hport,$thost,$tport = $line.split('|')
    Write-Host 'locatip='$hhost' localport='$hport' targetIP='$thost' targetPort='$tport
    $comnd = 'netsh interface portproxy add v4tov4 listenaddress='+$hhost+' listenport='+$hport+' connectaddress='+$thost+' connectport='+$tport
    #$comnd = 'netsh interface portproxy show all'
    #Write-Host $comnd
    iex $comnd
}

$comnd = 'netsh interface portproxy show all'
Write-Host 'Status'
iex $comnd
