use

https://github.com/majidh1/Mh1PersianDatePicker

#1
```
<link type="text/css" rel="stylesheet" href="Mh1PersianDatePicker.css" />
<script type="text/javascript" src="Mh1PersianDatePicker.js"></script>
```
#2
```
    <input type="text" onclick="Mh1PersianDatePicker.Show(this,'1398/01/21',window.holidays)" placeholder="onclick with holidays" />
    <input type="text" onfocus="Mh1PersianDatePicker.Show(this,'1398/01/21',)" placeholder="onfocus without holidays" />
    <input type="text" mh1pdp placeholder="script1 with holidays" />
    <input type="text" anyattr placeholder="script2 without holidays" />
```

-------

set to item
```
<input id='datepicker' style="background-color:black; color:white;" type="text" onclick="Mh1PersianDatePicker.Show(this,'1398/01/21',window.holidays)" placeholder="زمان را انتخاب کنید" />
```
in dynamyc action > when lose focus -> set value > type=javascript
```
document.getElementById('datepicker').value;
```
