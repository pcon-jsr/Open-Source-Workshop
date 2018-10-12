#!/bin/bash

#Given a directory, look for files having ".log" extension and contains the word "problem" anywhere inside.
#Copy such files to a temp sub-directory. If this directory already exists do nor re-create it.
#Directory location is passed as 1st argument while executing the script.

files=`ls $1/*.log`

mkdir -p $1/temp

for file in $files
do
	if [ `grep -l "problem" $file` ]; then
		echo $file
		cp $file $1/temp
	fi
done

#Single line command for the above code
#mkdir -p ./temp/temp && cp `find ./temp -maxdepth 1 -type f -name *.log -exec grep -l "problem" {} \;` ./temp/temp
