#!/bin/bash

#What does it need to do?
#connect to openvpn using my credentials
#start the SCRIPT
#Wait a little bit
#do it again!


cat << "EOF"

 ██████╗ █████╗ ██████╗ ██╗  ████████╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██╔══██╗██║  ╚══██╔══╝██╔═══██╗████╗  ██║
██║     ███████║██████╔╝██║     ██║   ██║   ██║██╔██╗ ██║
██║     ██╔══██║██╔══██╗██║     ██║   ██║   ██║██║╚██╗██║
╚██████╗██║  ██║██║  ██║███████╗██║   ╚██████╔╝██║ ╚████║
╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝    ╚═════╝ ╚═╝  ╚═══╝
       -----It's not unusual to be strange-----

Created by Denzilly - 2019
EOF





echo "Would you like to run the package installer? (Y/N)"
#read install

### RUN INSTALLER####
while true; do

  read install

  if [ "$install" == "Y" ] || [ "$install" == "y" ]; then
    #Install packages
    echo "test" | sudo pip install pyscreenshot bs4 sklearn pandas matplotlib numpy selenium
    echo "test" | sudo cp data/resources/geckodriver /usr/local/bin
    echo "test" | sudo pamac build nordconnect

    echo "Installation Complete"
    break
  elif [ "$install" == "N" ] || [ "$install" == "n" ]; then
    echo "continue as normal"
    break
  else
    echo "Please enter Y/N"






counter=1

#Initialise an array of all entries in ovpn_udp
vpns=()
for entry in `ls /etc/openvpn/ovpn_udp`;
do
    IFS="." read -ra strarr <<< "$entry"
    #echo "${strarr[0]}"
    vpns+=("${strarr[0]}")
done




#The loop
while [ $counter -le 10 ]

do

  echo "lets go"
  read varname
  #Let's select a VPN!



  #Connect to a VPN from the list
  echo test | sudo -b nordconnect ${vpns[$counter]}
  echo "Connection Established"
  echo "Running Carlton"
  echo test | sudo python carlton.py



  sleep 5
  echo "killing now"
  #Disconnect from vpn and kill stray firefox windows
  sudo killall -SIGINT openvpn
  sudo killall -SIGINT firefox


  echo $counter loops completed
