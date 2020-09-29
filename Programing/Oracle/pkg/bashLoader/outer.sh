#!/bin/bash

########### Variables
sleeptime=1
ready2loadpath="/icb/mediation/ready2load"
errorpath="/icb/mediation/error"
loadedpath="/icb/mediation/loaded"
loadingpath="/icb/archive"
logpath="/icb/mediation/logs"

########### main while
while [ $(ls ${ready2loadpath} |grep ".gz"| wc -l | awk '{print $1}') -gt 0 ]
do

  #echo $(ls ${loadingpath} | grep "lic_" | wc -l | awk '{print $1}')
  #echo $(ls ${logpath} | grep 'pid' | wc -l | awk '{print $1}')

  ########### check move to loading completed
  while [ $(ls ${loadingpath} | grep "lic_" | wc -l | awk '{print $1}') -gt 0 ] || [ $(ls ${logpath} | grep 'pid' | wc -l | awk '{print $1}') -gt 10 ]
  do
  	sleep ${sleeptime}
  	echo -e "pids: "$(ls ${logpath} | grep 'pid'  | wc -l | awk '{print $1}')" "
  done

  nohup bash worker.sh > /dev/null 2>&1 &

done

