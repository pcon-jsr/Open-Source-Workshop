#!/bin/bash

#Script to print 'n' fibonacci numbers
#'n' is entered as parameter while executing the script 

count=2
a=1
b=1
echo -n "$a $b "

while [ $count -lt $1 ]
do
	c=$(($a+$b))
	echo -n "$c "
	a=$b
	b=$c
	count=$(($count+1))
done
