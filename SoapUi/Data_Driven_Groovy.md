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

Workbook WorkBook1 = Workbook.getWorkbook(new File(FilePath))
Sheet Sheet1 = WorkBook1.getSheet(0)
PropertiesTestStep = TestCase.getTestStepByName("Properties")
count = PropertiesTestStep.getPropertyValue("Counter").toInteger()

if (PropertiesTestStep.getPropertyValue("Total").toString() == "")
	PropertiesTestStep.setPropertyValue("Total",Sheet1.getRows().toString())

count++

Cell Field1 = Sheet1.getCell(0, count)
Cell Field2 = Sheet1.getCell(1, count)
Cell Field3 = Sheet1.getCell(2, count)

log.info ("Count is " + count.toString() + " | IMSI : " + Field1.getContents() + " | KI : " + Field2.getContents() + " | MSISDN : " + Field3.getContents())
WorkBook1.close()

PropertiesTestStep.setPropertyValue("IMSI", Field1.getContents())
PropertiesTestStep.setPropertyValue("KI", Field2.getContents())
PropertiesTestStep.setPropertyValue("MSISDN", Field3.getContents())

if (count == PropertiesTestStep.getPropertyValue("Total").toInteger() - 1)
	PropertiesTestStep.setPropertyValue("End", "True")
	
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

PropertiesTestStep = TestCase.getTestStepByName("Properties")
Stop = PropertiesTestStep.getPropertyValue("End").toString()

if (Stop=="True")
	log.info("Exit Groovy Script - dataloop")
else
	testRunner.gotoStepByName("Groovy Script")
```
