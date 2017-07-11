#!/bin/bash

a="ffprobe ../test1.mov"

b="pwd"

c="ls"

ARRAY=($a)

rm out.txt
rm time.txt

for i in ${ARRAY[@]}
do 
	echo "${i}"
	{ time "${i}" &>> out.txt ; } 2>> time.txt
done

#{ time $a &>> out.txt ; } 2> time.txt
#{ time $b &>> out.txt ; } 2>> time.txt
