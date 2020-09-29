#!/bin/bash

########### Variables
psid=${$}
cyclenum="-n500"
ready2loadpath="/icb/mediation/ready2load"
errorpath="/icb/mediation/error"
loadedpath="/icb/mediation/loaded"
loadingpath="/icb/archive"
logpath="/icb/mediation/logs"
logfilename="lic_"${psid}

########### get file list
ls -l $ready2loadpath | head ${cyclenum} | sed '1d' | awk '{print $9,$5}' | sed 's/.gz//g' | tr ' ' ',' > ${loadingpath}"/"${logfilename}".txt"
echo "Started" > ${logpath}"/"${psid}".pid"


echo "psid="${psid}
########### DB insert list of files
sqlext=$(sqlplus p_torkanpour/P_t\#rk2@CPMPROD <<END
CREATE TABLE ${logfilename}
(
   FILE_NAME               VARCHAR2 (500),
   FILE_SIZE           VARCHAR2 (500)
)
ORGANIZATION EXTERNAL
   (TYPE ORACLE_LOADER
         DEFAULT DIRECTORY DIR_ICB
            ACCESS PARAMETERS (
               RECORDS DELIMITED BY NEWLINE
               SKIP 0
               FIELDS
                  TERMINATED BY ','
               MISSING FIELD VALUES ARE NULL
               REJECT ROWS WITH ALL NULL FIELDS
               (  FILE_NAME  char(200)               ,
   FILE_SIZE          char(200) )
            )
         LOCATION (
            DIR_ICB:'${logfilename}.txt'))
   REJECT LIMIT 0
   PARALLEL (DEGREE 4 INSTANCES 4);
INSERT INTO DWC_INPUT_FILE (FILE_NAME,
                               STATUS,
                               FILE_TYPE,
                               LOAD_ITEM_CD,
                               FILE_SIZE)
       SELECT file_name, 'ADDED', 'encode', '${psid}', file_size FROM ${logfilename};
Drop table ${logfilename} purge;
   exit;
END
)

########### mv files from Ready2load to loading
cat ${loadingpath}"/"${logfilename}".txt" | awk -F, '{print $1".gz"}' | xargs -I {} mv ${ready2loadpath}"/"{} ${loadingpath}  > /dev/null 2>&1
cat ${loadingpath}"/"${logfilename}".txt" | awk -F, '{print $1}' | xargs -I {} mv ${ready2loadpath}"/"{} ${loadingpath}  > /dev/null 2>&1
cat ${loadingpath}"/"${logfilename}".txt" | awk -F, '{print $1".gz"}' | xargs -I {} gunzip ${loadingpath}"/"{} > /dev/null 2>&1
mv ${loadingpath}"/"${logfilename}".txt" ${logpath}"/"${logfilename}".txt"

########### DB update status to Ready2load
sqlready=$(sqlplus p_torkanpour/P_t\#rk2@CPMPROD <<END
update dwc_input_file set status = 'READY2LOAD'
    where load_item_cd = '${psid}';
exit;
END
)

########### DB Start Procedure
getlist=$(sqlplus p_torkanpour/P_t\#rk2@CPMPROD <<END
exec PKG_ETL_UNL_FILES.LOAD_ONE_ITEM(${psid});
exit;
END
)
########### DB get list and status
sqlproc=$(sqlplus -S p_torkanpour/P_t\#rk2@CPMPROD <<END
set heading off
set feedback off
set pages 0
select FILE_NAME||','||STATUS from dwc_input_file
where load_item_cd = '${psid}';
exit;
END
)

echo $sqlproc | tr ' ' '\n' > ${logpath}"/db_"${logfilename}".txt"
########### MV files to loaded or error by status
while read  line
do
  fname=$(echo ${line}| awk -F, '{print $1}')
  status=$(echo ${line}| awk -F, '{print $2}')
  echo -en "."
  if [ ${status} = "LOADED" ]; then
    mv ${loadingpath}"/"${fname} ${loadedpath}"/"${fname}
  elif [ ${status} = "ERR_INSERT" ]; then
    mv ${loadingpath}"/"${fname} ${errorpath}"/"${fname}
  fi

done < ${logpath}"/db_"${logfilename}".txt"

rm ${logpath}"/"${psid}".pid"

