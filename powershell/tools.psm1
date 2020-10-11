function getIP{
    (Get-NetIPAddress -InterfaceAlias Ethernet0).IPv4Address
}
function sayhello{
    write-host("Hello, user!")