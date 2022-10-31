# Part 2

1.
```127.0.0.1 localhost
10.0.1.10 webserv1
10.0.1.11 webserv2```

2.
- From the proxy instance, the webservers can be accessed with their private IP's 
  - ```ssh -i .ssh/labsuser.pem ubuntu@webserv1```
  - ```ssh -i .ssh/labsuser.pem ubuntu@webserv2```
    - The hostname is able to be resolved from associating its private in the hosts file

