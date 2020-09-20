function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
$IP = getIP

$dat = (get-date -UFormat "%A %B %d, %Y")

$version = $HOST.Version.Major

$body = "This machine's IP is $IP . User is $env:USERNAME . Hostname is $env:COMPUTERNAME . PowerShell Version $version . Today's Date is $dat ."

Send-MailMessage -To "aknuth333@outlook.com" -From "aknuth333@outlook.com" -Subject "IT3038C Windows SysInfo" -Body $body -SmtpServer smtp.office365.com -port 587 -UseSsl -Credential (Get-Credential)
