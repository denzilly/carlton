#!/bin/bash

GOLD='\033[1;33m'
NC='\033[0m'


### RUN NORDVPN LOGIN TO ENTER CREDENTIALS ###

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





echo "####    Would you like to run the package installer? (Y/N)    ####"
#read install

### RUN INSTALLER####
while true; do

  read install

  if [ "$install" == "Y" ] || [ "$install" == "y" ]; then
    #Install packages
    echo "test" | sudo pip install pyscreenshot bs4 sklearn pandas matplotlib numpy selenium
    echo "test" | sudo cp data/resources/geckodriver /usr/local/bin
    echo "test" | sudo pamac build nordconnect
    
    cwd=$(pwd)

    echo "test" | sudo pacman -S openvpn
    cd /etc/openvpn
    echo "test" | sudo wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip
    echo "test" | sudo unzip ovpn.zip
    echo "test" | sudo rm ovpn.zip

    cd $cwd



    echo "####    Installation Complete    ####"
    break
  elif [ "$install" == "N" ] || [ "$install" == "n" ]; then
    echo "####    Continue as normal    ####"
    break
  else
    echo "####    Please enter Y/N    ####"


  fi

done

echo "How many votes would  you like to attempt? (max 5000, for now)"
read votes 
counter=1
echo "Where would you like to start in the vpn list (1-5000)?"
read vpnstart

#Initialise an array of all entries in ovpn_udp
vpns=()
for entry in `ls /etc/openvpn/ovpn_udp`;
do
    IFS="." read -ra strarr <<< "$entry"
    #echo "${strarr[0]}"
    vpns+=("${strarr[0]}")
done

echo test | sudo systemctl enable nordvpnd.service
echo test | sudo systemctl start nordvpnd.service
nordvpn login
nordvpn d


#The loop
while [ $counter -le $votes ]

do

  echo "#####    Connecting to a VPN with IP:   ####"

  #Let's select a VPN!
  curl ifconfig.me




  #Connect to a VPN from the list
  nordvpn connect ${vpns[$vpnstart]}
  echo "####    Connection Established    ####"
  echo "####    Running Carlton    ####"
  sleep 5
  curl ifconfig.me
  python carlton.py



  sleep 5
  echo "####    Killing Processes    ####"
  #Disconnect from vpn and kill stray firefox windows
  nordvpn disconnect
  sudo killall -SIGINT firefox


  echo $counter votes completed this session
  counter=$((counter+1))
  vpnstart=$((vpnstart+1))
done
