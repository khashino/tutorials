# use nifi with ldap (docker)

### first

```
docker pull osixia/openldap
```
then run container
```
docker run -p 389:389 -p 636:636 --name openldap2 --hostname ldap.bonyan.local --detach osixia/openldap:1.4.0
```
check the IP
```
docker exec -it openldap2 /bin/bash
  # check container IP
  ip a
```
### secound 
```
docker pull apache/nifi
```
fill the IP 
```
docker run --name nifi \
    --hostname nifi.bonyan.local \
    -v /root/cert:/opt/certs \
    -p 8443:8443 \
    -e NIFI_WEB_HTTP_HOST=nifi.bonyan.local\
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
    -e LDAP_URL='ldap://<IP/Host>:389' \
    -d \
    apache/nifi:latest 
```

then open 

https://localhost:8443/nifi/

```
user : admin
pass : admin
```
### third

https://hub.docker.com/r/michalklempa/nifi-registry

```
docker pull michalklempa/nifi-registry
```

```
docker run --name nifi-registry \
      -v /Users/khashayarnorouzi/tmp/cert/localhost:/opt/certs \
      -p 18443:18443 \
      -e 'NIFI_REGISTRY_SECURITY_KEYSTORE=/opt/certs/keystore.jks' \
      -e 'NIFI_REGISTRY_SECURITY_KEYSTOREtYPE=JKS' \
      -e 'NIFI_REGISTRY_SECURITY_KEYSTOREpASSWD=FyiozSPwniHe633Z+++QvH3HgirK4T9Pe4RILD+aKm4' \
      -e 'NIFI_REGISTRY_SECURITY_TRUSTSTORE=/opt/certs/truststore.jks' \
      -e 'NIFI_REGISTRY_SECURITY_TRUSTSTOREtYPE=JKS' \
      -e 'NIFI_REGISTRY_SECURITY_TRUSTSTOREpASSWD=LtLqii7LMYCpscMOHTGDHyJQABM3jnnbxYm72SQK+aE' \
      -e 'NIFI_REGISTRY_WEB_HTTP_HOST=' \
      -e 'NIFI_REGISTRY_WEB_HTTP_PORT=' \
      -e 'NIFI_REGISTRY_WEB_HTTPS_HOST=0.0.0.0' \
      -e 'NIFI_REGISTRY_WEB_HTTPS_PORT=18443' \
      -e 'INITIAL_ADMIN_IDENTITY=cn=admin,dc=example,dc=org' \
      -e 'NIFI_REGISTRY_SECURITY_IDENTITY_PROVIDER=ldap-identity-provider' \
      -e 'NIFI_REGISTRY_SECURITY_NEEDcLIENTaUTH=false' \
      -e 'LDAP_AUTHENTICATION_STRATEGY=SIMPLE' \
      -e 'LDAP_MANAGER_DN=cn=admin,dc=example,dc=org' \
      -e 'LDAP_MANAGER_PASSWORD=admin' \
      -e 'LDAP_USER_SEARCH_BASE=dc=example,dc=org' \
      -e 'LDAP_USER_SEARCH_FILTER=cn={0}' \
      -e 'LDAP_IDENTITY_STRATEGY=USE_DN' \
      -e 'LDAP_URL=ldap://<IP>:389' \
      -d \
      michalklempa/nifi-registry:latest
```

https://localhost:18443/nifi-registry
https://nifi.bonyan.local:18443/nifi-registry

### connect nifi to registry

https://docs.cloudera.com/HDPDocuments/HDF3/HDF-3.1.2/bk_user-guide/content/connecting-to-a-nifi-registry.html#:~:text=To%20connect%20NiFi%20to%20a,provide%20a%20name%20and%20URL.


### give permision to user in nifi

So, i've clicked the "manage access policies" item in the right-click menu of the canvas and added my user everywhere, and now I can use the UI.
