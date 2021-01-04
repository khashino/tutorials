### Installation
```
yum install -y epel-release
yum -y install nginx
```
installing njs
```
yum -y install njs
```
### Start
```
systemctl start nginx
systemctl status nginx
```
check server
```
http://<localhost/ip>
```


# Offiline

#

## Get NGINX source code
```bash
wget https://nginx.org/download/nginx-1.12.2.tar.gz
```

## Extract the source
```bash
tar xvzf nginx-1.12.2.tar.gz
```

## CD
```bash
cd ~/nginx-1.12.2
```

## Create nginx user
```bash
useradd nginx
usermod -s /sbin/nologin nginx
```

## Configure
```bash
./configure --user=nginx --group=nginx

....


Configuration summary
  + using system PCRE library
  + OpenSSL library is not used
  + using system zlib library

  nginx path prefix: "/usr/local/nginx"
  nginx binary file: "/usr/local/nginx/sbin/nginx"
  nginx modules path: "/usr/local/nginx/modules"
  nginx configuration prefix: "/usr/local/nginx/conf"
  nginx configuration file: "/usr/local/nginx/conf/nginx.conf"
  nginx pid file: "/usr/local/nginx/logs/nginx.pid"
  nginx error log file: "/usr/local/nginx/logs/error.log"
  nginx http access log file: "/usr/local/nginx/logs/access.log"
  nginx http client request body temporary files: "client_body_temp"
  nginx http proxy temporary files: "proxy_temp"
  nginx http fastcgi temporary files: "fastcgi_temp"
  nginx http uwsgi temporary files: "uwsgi_temp"
  nginx http scgi temporary files: "scgi_temp"
```

## Continue with MAKE
```bash
make
make install
```

## Starting and stopping NGINX
```bash
./nginx             ## To start nginx
./nginx -s stop     ## To stop nginx
```
