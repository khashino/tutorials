# Python Basics
installing package
```
pip install <PACKAGE>
```

### if statement
```
if (a>10):
  print("test")
elif(a<10):
  print("test")
else:
  print("test")

-----

==
<=
>
!=
...

```

### Iteration

#### while
```
count = 0
while(count<5)
  print(count)
  count = count + 1
```
#### for
```
count = 0
for count in range(1,10):
  print(count)

-----

names = ["X","Y"]
for count in len(names):
  print(names[count])

```

### Command line arguments
```
python test.py arg1 arg2
```
test.py:
```
print(sys.argv[x])
```
arg list :
```
arglist : ['test.py','arg1','arg2']
```

you can use argparser too
