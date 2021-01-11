Proccess after submit
```
/* Formatted on 12/13/2020 1:58:41 PM (QP5 v5.326) */
DECLARE
    Upload_blob   BLOB;
    file_text   CLOB;
     -----------loop----------------
    l_offset         PLS_INTEGER := 1;
    l_line           clob;
    l_total_length   PLS_INTEGER;
    l_line_length    PLS_INTEGER;
    l_clob           CLOB;

    ---------------
    col1            VARCHAR2 (4000);
    col2            VARCHAR2 (4000);
    col3           VARCHAR2 (4000);
    col4           VARCHAR2 (4000);
    col5            VARCHAR2 (4000);
    col6            VARCHAR2 (4000);
    col7           VARCHAR2 (4000);
    col8           VARCHAR2 (4000);
    col9            VARCHAR2 (4000);
    col10            VARCHAR2 (4000);
    
BEGIN
    --Copy BLOB to Upload_blob variable
    --raise_application_error(-20010,'test');
    SELECT blob_content
      INTO Upload_blob
      FROM APEX_APPLICATION_TEMP_FILES
     WHERE name = :P7_FILE_CHOOSE;
     
    --raise_application_error(-20010,'Upload_blob');
    
    --file_text := f(Upload_blob) ;
    
    select TO_CLOB(Upload_blob, 873, 'text/xml') into file_text from dual;

    --raise_application_error(-20010,file_text);

l_total_length := LENGTH(file_text);
WHILE l_offset <= l_total_length
    LOOP
        l_line_length := INSTR (file_text, CHR (10), l_offset) - l_offset;

        IF l_line_length < 0
        THEN
            l_line_length := l_total_length + 1 - l_offset;
        END IF;

        l_line := SUBSTR (file_text, l_offset, l_line_length);
        --DBMS_OUTPUT.put_line ('1' || l_line);

        SELECT REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              1)
                   cl1,
               REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              2)
                   cl2,
               REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              3)
                   cl3,
               REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              4)
                   cl4,
                   REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              5)
                   cl5,
               REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              6)
                   cl6,
               REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              7)
                   cl7,
               REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              8)
                   cl8,
                   REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              9)
                   cl9,
               REGEXP_SUBSTR (l_line,
                              '[^,]+',
                              1,
                              10)
                   cl10
            INTO col1,
               col2,
               col3,
               col4,
               col5,
               col6,
               col7,
               col8,
               col9,
               col10       
          FROM DUAL;
    --raise_application_error(-20010,fphone);
    -- شماره-نام-ایمیل-سن-جنسیت-استان-شهر-شرکت-تاریخ تولد-تاریخ مناسبت

        insert into STTC_CONTACT_NUMBER(CONTACT_ID,CONTACT_NUMBER,NAME,EMAIL,age,gender,province,city,company,BIRTHDAY,occasion_date)values(:P7_HIDDEN1,col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 );
        COMMIT;
        --DBMS_OUTPUT.put_line ('1' || fname);
        l_offset := l_offset + l_line_length + 1;
    END LOOP;

    l_offset := 1;
    COMMIT;
END;
```

then put upload file and submit butten
