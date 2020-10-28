https://www.youtube.com/watch?v=CT__W6qGU1Q

https://dev.maxmind.com/geoip/geoip2/geolite2/#Databases

### list of proccessors
```
1-GenerateFlowFile
2-UpdateAttribute
3-GeoEnrichIP
4-AttributeToJson
```
### Configs
#### 2-UpdateAttribute
Properties
```
add new property 
property=ipaddress
value=51.195.53.43
```
#### 3-GeoEnrichIP
Properties
```
MaxMidnDatabaseFile=...../city.mmdb
IPAddressAttribute=ipaddress
```
#### 4-AttributeToJson
Properties
```
Attribute List=ipaddress.geo.lookup.micros,ipaddress.geo.city,ipaddress.accuracy,ipaddress.geo.latitude,ipaddress.geo.longitude,ipaddress.geo.subdivision.0,ipaddress.geo.subdivision.isocode.0,ipaddress.geo.country,ipaddress.geo.country.isocode,ipaddress.geo.postalcode
Destination=flowfole-content
```
