#!/bin/bash

#What does it need to do?
#connect to openvpn using my credentials
#start the SCRIPT
#Wait a little bit
#do it again!




counter=1
while [ $counter -le 10 ]
do
echo $counter
((counter++))
done
echo All done
