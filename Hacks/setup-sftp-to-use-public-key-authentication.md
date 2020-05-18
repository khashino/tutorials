https://stackoverflow.com/questions/2231514/setup-sftp-to-use-public-key-authentication

# setup-sftp-to-use-public-key-authentication



In the client you need to generate its public key and add it to server's authorized key list.

The following are the commands you can use.

### On client machine
```
ssh-keygen -t dsa -f id_dsa
mv id_dsa* ~/.ssh/
scp ~/.ssh/id_dsa.pub USER_NAME@SERVER:~/.ssh/HOST_NAME.key
```
### On the server
```
cat ~/.ssh/HOST_NAME.key >> ~/.ssh/authorized_keys2
```
