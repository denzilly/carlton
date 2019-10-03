#!/bin/bash

#What does it need to do?
#connect to openvpn using my credentials
#start the SCRIPT
#Wait a little bit
#do it again!


#learn bash you turd

echo Welcome to carlton
echo "Would you like to run the package installer? (Y/N)"
#read install

### RUN INSTALLER####
while true; do

  read install

  if [ "$install" == "Y" ] || [ "$install" == "y" ]; then
    echo "run the installer"
    break
  elif [ "$install" == "N" ] || [ "$install" == "n" ]; then
    echo "continue as normal"
    break
  else
    echo "Please enter Y/N"

echo test | sudo python vpnlist.py



fi
done
