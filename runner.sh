#!/bin/bash

count=1
echo "test" | systemctl start tor.service
#The loop
while [ $counter -le 100 ]

do
  tor-browser &
  ./run_tor.sh
  sleep 15m
  echo "test" | sudo killall firefox.real
  count=$((counter+1))
  
done





