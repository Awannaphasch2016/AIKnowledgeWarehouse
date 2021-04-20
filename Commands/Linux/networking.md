:network:command:
* get wifi password from the internet
    * `netsh wlan show profile CarmelaGuests key=clear`

:network:ip-adress:ip:internal-ip-address:
* get internal ip address
    * `hostname -I `

:network:port:
* scan for listening port
    * ` netstat -ln | awk '{ if ($4 ~ /:80$/) print $0 }'` 
