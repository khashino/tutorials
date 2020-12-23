DECLARE


-- SOAP REQUESTS/RESPONSE
   soap_req_msg    VARCHAR2 (2000);
   soap_resp_msg   VARCHAR2 (2000);

   -- HTTP REQUEST/RESPONSE
   http_req        UTL_HTTP.req;
   http_resp       UTL_HTTP.resp;

BEGIN
   --
   -- Create SOAP request via HTTP
   --
   soap_req_msg := 
      '
      <soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:exam="http://example" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
   <soapenv:Header/>
   <soapenv:Body>
      <exam:enqueue soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <username xsi:type="xsd:string">cio5</username>
         <password xsi:type="xsd:string">test987</password>
         <domain xsi:type="xsd:string">cio5</domain>
         <msgType xsi:type="xsd:int">0</msgType>
         <messages xsi:type="exam:ArrayOf_xsd_string" soapenc:arrayType="xsd:string[]">
         	<item xsi:type="xsd:string">Sample-03-ORDB-SV41</item>
         </messages>
         <destinations xsi:type="exam:ArrayOf_xsd_string" soapenc:arrayType="xsd:string[]">
         	<item xsi:type="xsd:string">09127113260</item>
         </destinations>
         <originators xsi:type="exam:ArrayOf_xsd_string" soapenc:arrayType="xsd:string[]">
         	<item xsi:type="xsd:string">8937009</item>
         </originators>
         <udhs xsi:type="exam:ArrayOf_xsd_string" soapenc:arrayType="xsd:string[]">
         	<item xsi:type="xsd:string"/>
         </udhs>
         <mClass xsi:type="exam:ArrayOf_xsd_string" soapenc:arrayType="xsd:string[]">
         	<item xsi:type="xsd:string"/>
         </mClass>
      </exam:enqueue>
   </soapenv:Body>
</soapenv:Envelope>
      ';

   http_req :=UTL_HTTP.begin_request('http://10.20.11.200/websrv/services/SMS', 'POST', 'HTTP/1.1');
   UTL_HTTP.set_header (http_req, 'Accept-Encoding', 'gzip,deflate');
   UTL_HTTP.set_header (http_req, 'Content-Type', 'text/xml;charset=UTF-8');
   UTL_HTTP.set_header (http_req, 'Content-Length', length(soap_req_msg));
   --UTL_HTTP.set_header (http_req, 'Host', 'localhost:3038');
   --UTL_HTTP.set_header (http_req, 'Connection', 'Keep-Alive');
   --UTL_HTTP.set_header (http_req, 'User-Agent', 'Apache-HttpClient/4.1.1 (java 1.5)');
   UTL_HTTP.set_header (http_req, 'SOAPAction', '');
   UTL_HTTP.write_text (http_req, soap_req_msg);

  dbms_output.put_line(' ');
  --
   -- Invoke Request and get Response.
   --
   http_resp := UTL_HTTP.get_response(http_req);
   UTL_HTTP.read_text (http_resp, soap_resp_msg);
   UTL_HTTP.end_response (http_resp);
   DBMS_OUTPUT.put_line ('Output: ' || soap_resp_msg);
   Raise_Application_Error (-20343, soap_resp_msg);
END;
