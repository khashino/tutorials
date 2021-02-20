/* Formatted on 2/20/2021 2:51:16 PM (QP5 v5.362) */
WITH
    t 
    AS
        (SELECT '<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <soapenv:Body>
      <ns1:enqueueResponse xmlns:ns1="http://example" soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <enqueueReturn xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" soapenc:arrayType="xsd:long[2]" xsi:type="soapenc:Array">
            <enqueueReturn xsi:type="xsd:long">50959060</enqueueReturn>
            <enqueueReturn xsi:type="xsd:long">69822355</enqueueReturn>
         </enqueueReturn>
      </ns1:enqueueResponse>
   </soapenv:Body>
</soapenv:Envelope>' vCampo1
           FROM DUAL)
        SELECT a.*
          FROM t, 
               XMLTABLE (
                   xmlnamespaces ('http://schemas.xmlsoap.org/soap/envelope/' AS "soapenv",
                                  'http://example' AS "ns1"),
                   '/soapenv:Envelope/soapenv:Body/ns1:enqueueResponse/enqueueReturn/enqueueReturn'
                   PASSING xmltype (t.vCampo1)
                   COLUMNS 
                           msgid      VARCHAR2 (100) PATH '.') a;
