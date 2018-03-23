
###For installing VNC###
sudo apt-get install tightvncserver

###For Starting the VNCServer###
vncserver :1 -geometry 1920x1080 -depth 24

###For port encapsulation###
This encapsulates VNC traffic with SSH
"ssh -L 127.0.0.1:"random desired port":192.168.1.100:5901 "currentuser"@"ip"