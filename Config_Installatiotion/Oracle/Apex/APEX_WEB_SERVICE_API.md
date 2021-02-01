
#MAKE_REST_REQUEST Function
Use this function to invoke a RESTful style Web service supplying either name value pairs, a character based payload or a binary payload and returning the response in a CLOB.

Syntax
```
APEX_WEB_SERVICE.MAKE_REST_REQUEST(
    p_url               IN VARCHAR2,
    p_http_method       IN VARCHAR2,
    p_username          IN VARCHAR2 default null,
    p_password          IN VARCHAR2 default null,
    p_proxy_override    IN VARCHAR2 default null,
    p_transfer_timeout  IN NUMBER   default 180,
    p_body              IN CLOB default empty_clob(),
    p_body_blob         IN BLOB default empty_blob(),
    p_parm_name         IN apex_application_global.VC_ARR2 default empty_vc_arr,
    p_parm_value        IN apex_application_global.VC_ARR2 default empty_vc_arr,
    p_wallet_path       IN VARCHAR2 default null,
    p_wallet_pwd        IN VARCHAR2 default null ) 
RETURN CLOB;
```
###Parameters
Describes the parameters available in the MAKE_REST_REQUEST function.
```
Parameter	Description
p_url

The URL endpoint of the Web service.

p_http_method

The HTTP method to use, PUT, POST, GET, HEAD, or DELETE.

p_username

The username if basic authentication is required for this service.

p_password

The password if basic authentication is required for this service

p_proxy_override

The proxy to use for the request. The proxy supplied overrides the proxy defined in the application attributes.

p_transfer_timeout

The amount of time in seconds to wait for a response.

p_body

The HTTP payload to be sent as CLOB.

p_body_blob

The HTTP payload to be sent as binary BLOB. For example, posting a file.

p_parm_name

The name of the parameters to be used in name/value pairs.

p_parm_value

The value of the parameters to be used in name/value pairs.

p_wallet_path

The file system path to a wallet if the URL endpoint is https. For example, file:/usr/home/oracle/WALLETS. The wallet path provided overrides the wallet defined in the instance settings.

p_wallet_pwd

The password to access the wallet.
```

##Example

The following example calls a RESTful style Web service using the make_rest_request function passing the parameters to the service as name/value pairs. The response from the service is stored in a locally declared CLOB.
```
declare
    l_clob       CLOB;
BEGIN
 
    l_clob := apex_web_service.make_rest_request(
        p_url => 'http://us.music.yahooapis.com/ video/v1/list/published/popular',
        p_http_method => 'GET',
        p_parm_name => apex_util.string_to_table('appid:format'),
        p_parm_value => apex_util.string_to_table('xyz:xml'));
 
END
```
## Ex2
```
declare
    l_clob       CLOB;
    l_body  clob;
BEGIN
    l_body :=to_clob('<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:urn="urn:smspushinterface">
    <soapenv:Header/>
    <soapenv:Body>
        <urn:SMSSubmitReq>
            <urn:Sender>
                <urn:Username>xxx</urn:Username>
                <urn:Password>xxxxxxx</urn:Password>
                <urn:Address>xxx</urn:Address>
                <urn:ID>xxx</urn:ID>
                <urn:MessageTypeID>SMS</urn:MessageTypeID>
            </urn:Sender>
            <urn:Recipient>
                <urn:Number>xxxxx</urn:Number>
            </urn:Recipient>
            <urn:MsgDetails>
                <urn:MsgType>0</urn:MsgType>
                <urn:ShortMessage>test</urn:ShortMessage>
                <urn:MsgPriority>0</urn:MsgPriority>
            </urn:MsgDetails>
        </urn:SMSSubmitReq>
    </soapenv:Body>
</soapenv:Envelope>');
 
    l_clob := apex_web_service.make_rest_request(
        p_url => 'http://xxx.xx.xx.xxx:xxx/xxxx/xxxx',
        p_http_method => 'POST',
        p_body => l_body
        );

    display(l_clob);
 
END
```
