# use nifi with ldap (docker)

first
```
docker run -p 389:389 -p 636:636 --name openldap2 --detach osixia/openldap:1.4.0
docker exec -it openldap2 /bin/bash
  # check container IP
  ip a
```
secound 

fill the IP 
```
docker run --name nifi \
  -v /Users/khashayarnorouzi/tmp/cert/localhost:/opt/certs \
  -p 8443:8443 \
  -e AUTH=ldap \
  -e KEYSTORE_PATH=/opt/certs/keystore.jks \
  -e KEYSTORE_TYPE=JKS \
  -e KEYSTORE_PASSWORD=FyiozSPwniHe633Z+++QvH3HgirK4T9Pe4RILD+aKm4 \
  -e TRUSTSTORE_PATH=/opt/certs/truststore.jks \
  -e TRUSTSTORE_PASSWORD=LtLqii7LMYCpscMOHTGDHyJQABM3jnnbxYm72SQK+aE \
  -e TRUSTSTORE_TYPE=JKS \
  -e INITIAL_ADMIN_IDENTITY='cn=admin,dc=example,dc=org' \
  -e LDAP_AUTHENTICATION_STRATEGY='SIMPLE' \
  -e LDAP_MANAGER_DN='cn=admin,dc=example,dc=org' \
  -e LDAP_MANAGER_PASSWORD='admin' \
  -e LDAP_USER_SEARCH_BASE='dc=example,dc=org' \
  -e LDAP_USER_SEARCH_FILTER='cn={0}' \
  -e LDAP_IDENTITY_STRATEGY='USE_DN' \
  -e LDAP_URL='ldap://<IP>:389' \
  -d \
  apache/nifi:latest 
```

then open 

https://localhost:8443/nifi/

```
user : admin
pass : admin
```


