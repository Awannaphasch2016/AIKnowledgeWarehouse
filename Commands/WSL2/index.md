:display:wsl2:x11:
* use ip addres that is listed inresolv.conf againt the nameserver to expose 
    to x11 forwarding protocol.
    * export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"

:display:wsl1:x11:
* how to display graphic in wsl1 using x11 forwarding protocol
    * `export DISPLAY=localhost:0.0`
