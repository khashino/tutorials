 Map a FTP server as a Local Disk Drive

https://www.ferrobackup.com/map-ftp-as-disk.html

download link:

https://www.ferrobackup.com/download.html#ftpuse

Examples
```
To map (assign) the F: drive letter to the ftp.intel.com root folder, type:

FTPUSE F: ftp.intel.com

To assign the disk-drive device name F: to the Pub folder on the ftp.intel.com server as if the connection were made from the anonymous user account , type:

FTPUSE F: ftp.intel.com/Pub ftpuse@example /USER:anonymous

To execute the command in the background, type:

FTPUSE F: ftp.intel.com /HIDE

To delete the mapped disk drive, type:

FTPUSE F: /DELETE 
```
