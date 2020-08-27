```
-TestCase
  -testSteps
    1-Groovy Script
    2-Properties
    3-SoapXml
    4-Groovy Script - Dataloop
```
### 0

first download jxl.jar 
```
JExcelAAPI: https://sourceforge.net/projects/jexcelapi/files/jexcelapi/2.6.12/jexcelapi_2_6_12.zip/download
```
and put it in 
```
<SoapUi>\bin\ext
```
then reset SoapUI

### 1
```
import jxl.*

def TestCase = context.testCase
def FilePath = "C:\\Users\\khashayar\\Desktop\\soap.xls"
def count
File file = new File("C:\\Users\\khashayar\\Desktop\\soap.txt")

def threadIndex = context.ThreadIndex;
//System.out.println("Hi, I'm thread "+threadIndex);

Workbook WorkBook1 = Workbook.getWorkbook(new File(FilePath))
Sheet Sheet1 = WorkBook1.getSheet(0)
PropertiesTestStep = TestCase.getTestStepByName("Properties")
count = PropertiesTestStep.getPropertyValue("Counter").toInteger()

if (PropertiesTestStep.getPropertyValue("Total").toString() == "")
	PropertiesTestStep.setPropertyValue("Total",Sheet1.getRows().toString())

count++
PropertiesTestStep.setPropertyValue("Counter",count)


Cell Field1 = Sheet1.getCell(0, (threadIndex*20)+count)
Cell Field2 = Sheet1.getCell(1, (threadIndex*20)+count)
Cell Field3 = Sheet1.getCell(2, (threadIndex*20)+count)

//log.info ("Count is " + count.toString() + " | IMSI : " + Field1.getContents() + " | KI : " + Field2.getContents() + " | MSISDN : " + Field3.getContents())
Date latestdate = new Date();
file.append( latestdate.format("hh:mm:ss aa", TimeZone.getTimeZone("GMT+4:30")) + ",SendReq,SoapUI," + Field3.getContents()+","+threadIndex+"\n")
log.info ( latestdate.format("hh:mm:ss aa", TimeZone.getTimeZone("GMT+4:30")) + ",SendReq,SoapUI" + Field3.getContents())
WorkBook1.close()

PropertiesTestStep.setPropertyValue("IMSI", Field1.getContents())
PropertiesTestStep.setPropertyValue("KI", Field2.getContents())
PropertiesTestStep.setPropertyValue("MSISDN", Field3.getContents())

if (count == 20 )
	PropertiesTestStep.setPropertyValue("Counter", 0)
	//PropertiesTestStep.setPropertyValue("End", "True")
	
	
```
### 2
```
IMSI=null
MSISDN=null
KI=null
Total=null
End=false
Counter=0
```
### 3
use these for values
```
${Properties#IMSI}
${Properties#MSISDN}
${Properties#KI}
```
### 4
```
def TestCase = context.testCase
File file = new File("C:\\Users\\khashayar\\Desktop\\soap.txt")
PropertiesTestStep = TestCase.getTestStepByName("Properties")
Stop = PropertiesTestStep.getPropertyValue("End").toString()
msisdn = PropertiesTestStep.getPropertyValue("MSISDN").toString()

Date latestdate = new Date();
file.append( latestdate.format("hh:mm:ss aa", TimeZone.getTimeZone("GMT+4:30")) + ",GetRes,SoapUI," + msisdn.toString()+"\n")
log.info ( latestdate.format("hh:mm:ss aa", TimeZone.getTimeZone("GMT+4:30")) + ",GetRes,SoapUI," + msisdn.toString())

if (Stop=="True")
	log.info("Exit Groovy Script - dataloop")
else
	testRunner.gotoStepByName("Groovy Script")
  
```
### write to file
```
File file = new File("C:\\Users\\khashayar\\Desktop\\soap.txt")
file.write "First line\n"
file.append("hello\n")
file << "Second line\n"
 
println file.text
```
