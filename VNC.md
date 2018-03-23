
###For installing VNC###
sudo apt-get install tightvncserver

###For Starting the VNCServer###
vncserver :1 -geometry 1920x1080 -depth 24

###For port encapsulation###
This encapsulates VNC traffic with SSH
```shell
ssh -L 127.0.0.1:"random desired port":192.168.10.10:5901 "currentuser"@"ip"
```

Enter this command. If you connect successfully over SSH you can then open a vnc viewer of your choice and connect to the local ip of the machine. 

Example:
    vnc://127.0.0.1:5999