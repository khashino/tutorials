#!/bin/bash

echo "record system status"
echo "every "${1}" Secound"
echo "for "${2}" time" 
echo "output folder "${3}
echo -e " \n"

sar -u ${1} ${2} > ${3}/cpu.txt &
sar -r ${1} ${2} > ${3}/memory.txt &
sar -b ${1} ${2} > ${3}/disk.txt &
sar -n DEV ${1} ${2} > ${3}/net.txt && echo -e "\nDone"

echo -e "\n Agregate..."
echo "-------CPU------" > ${3}/total.txt
cat ${3}/cpu.txt >> ${3}/total.txt
echo "-------MEMORY------" >> ${3}/total.txt
cat ${3}/memory.txt >> ${3}/total.txt
echo "-------DISK------" >> ${3}/total.txt
cat ${3}/disk.txt >> ${3}/total.txt
echo "-------NET------" >> ${3}/total.txt
cat ${3}/net.txt >> ${3}/total.txt
sed -i 's/[[:space:]]\{2,\}/,/g' ${3}/total.txt

echo -e "\nDone \noutput: "${3}"/total.txt"


