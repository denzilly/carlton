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


#Install packages
echo "test" | sudo pip install pyscreenshot bs4 sklearn pandas matplotlib numpy selenium
echo "test" | sudo cp data/resources/geckodriver /usr/local/bin
echo "test" | sudo pamac build nordconnect


echo "installation complete"



counter=1

while [ $counter -le 10 ]

do

echo "lets go"
read varname
#source ./vpn.sh
echo test | sudo -b nordconnect nl467
echo "we made it through"
echo test | sudo python carlton.py



sleep 5
echo "killing now"
# stop the service
sudo killall -SIGINT openvpn
sudo killall -SIGINT firefox


echo $counter loops completed
