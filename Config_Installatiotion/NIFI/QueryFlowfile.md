https://www.youtube.com/watch?v=F2lH024LduE
## 1-GenerateFlowFile

custom text :
```
EId|PId|IP|Desc
1|Test|51.195.53.43|"MyIP"
2|Test|51.195.53.43|"MyIP"
3|Test|51.195.53.43|"MyIP"
```
## 2-UpdateAttribute

add-new property
```
property=schema.name
Value=myschema
```

### schemaValue
```
{
 "name": "myschema",
 "namespace": "nifi",
 "type": "record",
 "fields": [
 {"name": "EId" , "type" : "string"},
 {"name": "PId" , "type" : "string"},
 {"name": "Date" , "type" : "string"},
 {"name": "Desc" , "type" : "string"}
 ]
}
```
## 3-QueryRecord
Property
```
RecordReader = CsvReader
  setting:
    set Schema Registery = AvroReader
    Sepratro = |
    
    then config Avro 
    create new property
    property = schema
    value= ### schemaValue
    
    then enable avro
    
    Schema Access Strategy = Use Schema Name Property
    
    Enable CsvReader
    
RecordWriter = JsonWriter
  setting:
    Schema Write Strategy = schema name attribute
    Schema access Strategy = schema name property
    Schema Registy = select avro
    
    Enable It
    
new property
  property = ID2
  value = select * from FLOWFILE where EId='2'
  or
  select "Date" from FLOWFILE where EId='2'
 
```


## 4-LogAttribute
one for ID2
and one for other

