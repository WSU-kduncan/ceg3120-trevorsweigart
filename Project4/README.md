# Part 2

1.
```
127.0.0.1 localhost
10.0.1.10 webserv1
10.0.1.11 webserv2
```

2.
- From the proxy instance, the webservers can be accessed with their private IP's 
  - ssh -i .ssh/labsuser.pem ubuntu@webserv1
  
  - ssh -i .ssh/labsuser.pem ubuntu@webserv2

- The hostname is able to be resolved from associating its private in the hosts file

3.
- Files modified:
  - /etc/haproxy/haproxy.cfg

- Added to /etc/haproxy/haproxy:
  ```
  frontend myfrontend
    bind :80
  
  backend myservers
    server server1 10.0.1.10
    server server2 10.0.1.11
  ```
- Restarting haproxy
  - sudo systemctl restart haproxy

- Resources used:
  - https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/

4.
- No files were modified for the webserver

- No configurations were set

- The root directive is set to /var/www/html for the default nginx config

- Restarting nginx after config changes:
  - sudo systemctl reload nginx

- Resources used:
  - man /etc/nginx/nginx.conf

5.
- ![webserv1](webserv1.png)

- ![webserv2](webserv2.png)
