#!/bin/bash

###########################
fullpath=${1}
pid=${$} 
outpath="/icb/bmd/pgw"
javapath="/icb/bmd/scripts/temp/jre1.8.0_241/bin"
jarpath="/icb/bmd/scripts/temp/bonyanasn1.jar"
logpath=$outpath/logs
stagepath=$outpath/stage
processedpath=$outpath/processed
csvpath=$outpath/csv
filename=${fullpath##*/}
filename=${filename/.dat.gz/}
############################

echo $filename > ${logpath}/inner_${pid}.pid

mv ${fullpath} ${stagepath}
gunzip ${stagepath}/${filename}.dat.gz
${javapath}/java -cp ${jarpath} com.bonyansystem.App -csv -ifile ${stagepath}/${filename}.dat -odir ${csvpath}
mv ${stagepath}/${filename}.dat ${processedpath}/${filename}.dat

rm -f ${logpath}/inner_${pid}.pid

