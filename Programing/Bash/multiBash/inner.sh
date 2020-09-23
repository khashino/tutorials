#!/bin/bash

##########################
outpath="/icb/bmd/pgw"
logpath=$outpath/logs
filespath="/icb/bmd/rating/data/PGW"
outputpath=""
threadcount=10
sleeptime=1
cnt=0

##########################
for var in "$@"
do
	#echo $var
	#cnt=$((cnt+1))
	curfile=$var
	echo -e "start,"${curfile}","$(date +"%Y%m%d,%H%M%S")"" >> ${logpath}/totlog.log
	myfile=${filespath}/${curfile}
	
	nohup bash worker.sh ${filespath}/${curfile} > /dev/null 2>&1 &&echo -e "end,"${curfile}","$(date +"%Y%m%d,%H%M%S") >> ${logpath}/totlog.log  & 
	#echo "cnt: "$cnt
	#echo -n "."
	#while [ -f ${myfile} ] || [ $(ls ${logpath}/inner_*.pid | wc -l | awk '{print $1}') -gt ${threadcount} ]
	#while [ $(ls ${logpath}/inner_*.pid | wc -l | awk '{print $1}') -gt ${threadcount} ]
	#do	
	#	sleep ${sleeptime}
	#done
done