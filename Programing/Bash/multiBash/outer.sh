#!/bin/bash

##########################
outpath="/icb/bmd/pgw"
logpath=$outpath/logs
filespath="/icb/bmd/rating/data/PGW"
threadcount=20
sleeptime=0
counter=0
##########################

while [ 1 -eq 1 ]
do
	files=$(ls $filespath | head -n10 | grep .dat.gz | tr '\n' '\t' )
	counter=$((counter+10))
	#lists=$(cat $logpath/listfile.log)
	
	bash inner.sh ${files}

	while [ $(ls ${logpath}/inner_*.pid | wc -l | awk '{print $1}') -gt ${threadcount} ]
	do	
		sleep ${sleeptime}
		echo -e "pids: "$(ls ${logpath}/inner_*.pid | wc -l | awk '{print $1}')" count: "${counter}
		
	done


	
done
