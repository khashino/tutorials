# CurlMail
Sending Mail with curl command

you can change sender mail address subject & ...

## usage
first You should create html file and fill it like this sample :
```
From: Test Address <your-email_at_domain.com>
Reply-To: Test Address <your-email_at_domain.com>
To: libcurl development <curl-library_at_cool.haxx.se>
Subject: Test Email
Date: Mon, 09 Jan 2012 10:00:00 +0000
Content-Type: text/html; charset="us-ascii"
Content-Transfer-Encoding: quoted-printable
Mime-version: 1.0

<html>
<head>
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Dus-ascii">
</head>
<body>
<p>Hello World</p>
</body>
</html>
```
then you can save it and send it like this
```
curl  --mail-from "yourmail@domain.com" --mail-rcpt "YourTargetMail" --url smtps://YourMailSv/:465 --upload-file test.html(YourHTML)  --user "YourMailUser:YourPass" -v -k
```
