```
BEGIN

  DBMS_NETWORK_ACL_ADMIN.create_acl (
    acl          => 'utl_sms_mci.xml', 
    description  => 'access to sms mci server',
    principal    => 'BULK_SMS',
    is_grant     => TRUE, 
    privilege    => 'connect',
    start_date   => SYSTIMESTAMP,
    end_date     => NULL);

  COMMIT;

END;

--add the privilege to resolve names

BEGIN

  DBMS_NETWORK_ACL_ADMIN.add_privilege (
    acl          => 'utl_sms_mci.xml', 
    principal    => 'BULK_SMS',
    is_grant     => TRUE, 
    privilege    => 'resolve');

  COMMIT;

END;

--assign your mailserver

BEGIN

  DBMS_NETWORK_ACL_ADMIN.assign_acl (
    acl => 'utl_sms_mci.xml',
    host => '10.20.37.11', 
    lower_port => 80,
    upper_port => NULL); 
    commit;

END;


  BEGIN

  DBMS_NETWORK_ACL_ADMIN.assign_acl (
    acl => 'utl_sms_mci.xml',
    host => '10.20.37.11', 
    lower_port => 80,
    upper_port => NULL); 

  COMMIT;

  END;

  --more housekeeping

  alter system set sms_mci_out_server = '10.20.37.11:80' scope = both;

 --make sure the user can access the sms_mci packages

 GRANT EXECUTE ON UTL_TCP TO BULK_SMS;
 GRANT EXECUTE ON UTL_sms_mci TO BULK_SMS;
 GRANT EXECUTE ON UTL_MAIL TO BULK_SMS;

--check your work

select * from dba_network_acls;

--verify permissions for your user

SELECT DECODE(
DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE(
   'utl_sms_mci.xml', 'BULK_SMS', 'resolve'),
1, 'GRANTED', 0, 'DENIED', NULL) PRIVILEGE 
FROM DUAL;

--if you have created access permissions you wish to delete
--using the information from the select use this to delete what you don't want

exec DBMS_NETWORK_ACL_ADMIN.DROP_ACL ('acl_utl_sms_mci.xml');

--for more troubleshooting try this barebones mail procedure, run with your user. Copied from [here][1]
DECLARE
v_From      VARCHAR2(80) := 'oracle@mycompany.com';
v_Recipient VARCHAR2(80) := 'test@mycompany.com';
v_Subject   VARCHAR2(80) := 'test subject';
v_Mail_Host VARCHAR2(30) := 'mail.mycompany.com';
v_Mail_Conn utl_sms_mci.Connection;
crlf        VARCHAR2(2)  := chr(13)||chr(10);
BEGIN
v_Mail_Conn := utl_sms_mci.Open_Connection(v_Mail_Host, 25);
utl_sms_mci.Helo(v_Mail_Conn, v_Mail_Host);
utl_sms_mci.Mail(v_Mail_Conn, v_From);
utl_sms_mci.Rcpt(v_Mail_Conn, v_Recipient);
utl_sms_mci.Data(v_Mail_Conn,
'Date: '   || to_char(sysdate, 'Dy, DD Mon YYYY hh24:mi:ss') || crlf ||
'From: '   || v_From || crlf ||
'Subject: '|| v_Subject || crlf ||
'To: '     || v_Recipient || crlf ||
crlf ||
'some message text'|| crlf ||   -- Message body
'more message text'|| crlf
 );
utl_sms_mci.Quit(v_mail_conn);
EXCEPTION
WHEN utl_sms_mci.Transient_Error OR utl_sms_mci.Permanent_Error then
raise_application_error(-20000, 'Unable to send mail', TRUE);
END;
```
```
select p.principal,a.ACL,a.host,a.lower_port,a.upper_port,p.privilege,p.is_grant,p.invert,p.start_date,p.end_date from dba_network_acls a join dba_network_acl_privileges p on a.aclid = p.aclid;

BEGIN

  DBMS_NETWORK_ACL_ADMIN.add_privilege (
    acl          => 'utl_sms_mci.xml', 
    principal    => 'APEX_200200',
    is_grant     => TRUE, 
    privilege    => 'resolve');

  COMMIT;

END;



BEGIN

  DBMS_NETWORK_ACL_ADMIN.add_privilege (
    acl          => 'utl_sms_mci.xml', 
    principal    => 'APEX_200200',
    is_grant     => TRUE, 
    privilege    => 'connect');

  COMMIT;

END;
```
