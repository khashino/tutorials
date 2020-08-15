### Add njs module
add this in 

/etc/nginx/nginx.conf

```
load_module modules/ngx_http_js_module.so
```
### Conf sample
test.conf
```
js_include conf.d/header_logging.js;

server {
    listen       80;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    location /nginx_status {
          	stub_status;
    }

    location /return {
        default_type application/json;
        return 200 'gangnam style!11';
    }

    location /proxy {
        proxy_set_header Host              $http_host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-phone-header test;
        proxy_pass http://192.168.137.19:3001/;
    }

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```
### js Sample
header_logging.js
```
function kvHeaders(headers, parent) {
    var kvpairs = "";
    for (var h in headers) {
        kvpairs += " " + parent + "." + h + "=";
        if ( headers[h].indexOf(" ") == -1 ) {
		kvpairs += headers[h];
        } else {
            kvpairs += "'" + headers[h] + "'";
        }
    }
    return kvpairs;
}

function kvAccessLog(r) {
    var log = r.variables.time_iso8601;    // NGINX JavaScript can access all variables
    log += " client=" + r.remoteAddress;   // Property of request object
    log += " method=" + r.method;          // "
    log += " uri=" + r.uri;                // "
    log += " status=" + r.status;          // Property of response object
    log += kvHeaders(r.headersIn, "in");  // Send request headers object to function
    log += kvHeaders(r.headersOut, "out"); // Send response headers object to function
    //log += " byte:"+r.request_length
    return log;
}


function test(r) {
	return 200;
}


function api(r) {
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
             alert(this.responseText);
         }
    };
    xhttp.open("GET", "/status=check", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send("Your JSON Data Here");
}
```
