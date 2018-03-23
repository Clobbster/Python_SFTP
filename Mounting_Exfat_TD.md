###Install utility for ExFat TDs###
sudo apt-get install exfat-fuse exfat-utils

###Mounting Instructions###
sudo mkdir /media/"Example"
sudo mount -t auto /dev/sda1 /media/"Example"