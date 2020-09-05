first Create folder ssl in nginx folder
```
mkdir /etc/nginx/ssl
```
genarate self sign cert
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/pv-nginx-selfsigned.key -out /etc/nginx/ssl/nginx-selfsigned.crt
```
edit config file
```
server {
        listen              443 ssl;
        server_name         _;
        keepalive_timeout   70;

        ssl_certificate     /etc/nginx/ssl/nginx-selfsigned.crt;
        ssl_certificate_key /etc/nginx/ssl/pv-nginx-selfsigned.key;
        ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers         HIGH:!aNULL:!MD5;
        #...

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }
}


```
https://www.cloudsavvyit.com/1306/how-to-create-and-use-self-signed-ssl-on-nginx/
# OR
use

https://certbot.eff.org/


