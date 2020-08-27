groovy
```
def TestCase = context.testCase

PropertiesTestStep = TestCase.getTestStepByName("Properties")

month = PropertiesTestStep.getPropertyValue("MONTH").toInteger()
mo = PropertiesTestStep.getPropertyValue("MO").toInteger()
ye = PropertiesTestStep.getPropertyValue("YE").toInteger()

if (mo == 12){
	mo = 0
	ye++
}
if (month == 139903){
	mo = 10
	ye = 1397
}
mo++ 
month = (ye*100)+mo
log.info ("Month : " + month)

PropertiesTestStep.setPropertyValue("MONTH", month.toString())
PropertiesTestStep.setPropertyValue("MO", mo.toString())
PropertiesTestStep.setPropertyValue("YE", ye.toString())
```
