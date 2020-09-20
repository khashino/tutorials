#!/bin/bash

gateway=$(ifconfig | grep 'inet 192' | awk '{print $2}' | awk -F'.' '{print $1"."$2"."$3".0/24"}')
echo "gateway : "$gateway

if ! nmap -v COMMAND &> /dev/null
then
    echo -e "---------\nnmap could not be found\nuse:\n--------\napt-get install nmap\n--------\nthen run again"
    exit
fi

echo "Starting ..."

#hosts=nmap -sn $gateway| grep Nmap | awk '{print $5,$6}' | sed '1,1d;$d'
hosts=( $( nmap -sn $gateway| grep Nmap | awk '{print $5}' | sed '1,1d;$d') )
hosts_length=${#hosts[@]}

echo "Total host found : "$hosts_length

for i in "${hosts[@]}"
do
	echo -n $i" : "
  nmap $i | grep "/tcp" | awk '{print $1}' | awk -F'/' '{print $1}' | tr '\n' '|'
  echo ""
done
