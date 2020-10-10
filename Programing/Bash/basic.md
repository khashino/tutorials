# bash programing Basics

### Command line arguments

```
$# : number of arguments
$@ : all arguments
$0 : your bash file name
$$ : Process ID
$USER : The username of the user running the script.
$HOSTNAME : The hostname of the machine the script is running on.
$SECONDS : The number of seconds since the script was started.
$RANDOM : Returns a different random number each time is it referred to.
$LINENO - Returns the current line number in the Bash script.
$1 : First argument
$2 : Second argument
...
```

### Variables

```
myvariable='test'
anothervar='test2'
echo $myvariable $anothervar
```

### if statement

#### String

```
if [ "foo" = "foo" ]; then
  echo test1
else
  echo test2
fi

-----

T1="foo"
T2="bar"
if [ "$T1" = "$T2" ]; then
  echo test
else
  echo test2
fi

-----

if [ -n $var ]  # if null return true
if [ -z $var ]  # if empty return true

-----

= : equal
!= : not equal
\< : alphabet order
\> : alphabet order

```

#### Number

```
a=1
b=2
if [ "$a" -lt "$b" ]; then
  echo test1
else
  echo test2
fi

-----

-lt : less than
-le : less than or equal
-gt : greater than
-ge : greater than or equal
<>  : different
-ne : different

```

### For Loop

```
for i in {1..10}
do
  command
done  

-----

in 1 2 3 4 5 .. N
in file1 file2 file3
in $(Linux-Or-Unix-Command-Here)
in {0..10..2} # {START..END..INCREMENT}
in {1..5}
in $(seq 1 2 20)

-----

for (( ; ; ))
do
   echo "infinite loops [ hit CTRL+C to stop]"
done

-----

(( c=1; c<=5; c++ ))

```

### While Loop

```
while [ condition ]
do
   command
done

----

condition same as if conditions
```

sample reaad from file loop
```
while read  line
do
  Commands
done < file.txt
```

### Simple pinger.sh

```
#/bin/bash

for ip in $(seq 1 255)
do
        #echo "test "$1.$ip
        ping $1.$ip -c 1 | grep 64 | cut -d " " -f 4 | tr -d ":" &
done
```
