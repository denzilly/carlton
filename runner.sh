#!/bin/bash

count=1
loops=100
echo "test" | systemctl start tor.service
#The loop

while [[ $counter -le $loops ]]
do
  tor-browser &
  ./run_tor.sh
  sleep 15m
  echo "test" | sudo killall firefox.real
  count=$((counter+1))
  
done





