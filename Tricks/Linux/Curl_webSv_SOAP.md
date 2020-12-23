

# step1
create request.xml:
```
<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:exam="http://example" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
   <soapenv:Header/>
   <soapenv:Body>
      <exam:enqueue soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <username xsi:type="xsd:string">cio5</username>
         <password xsi:type="xsd:string">test987</password>
         <domain xsi:type="xsd:string">cio5</domain>
         <msgType xsi:type="xsd:int">0</msgType>
         <messages xsi:type="exam:ArrayOf_xsd_string" soapenc:arrayType="xsd:string[]">
         	<item xsi:type="xsd:string">Sample-02-Lin-SV41</item>
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
```

# step2

```
curl --header "Content-Type: text/xml;charset=UTF-8" --header "POST http://10.20.11.200/websrv/services/SMS HTTP/1.1" --header "SOAPAction:;" --data @request.xml http://10.20.11.200/websrv/services/SMS

```
