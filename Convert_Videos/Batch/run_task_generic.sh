#!/bin/bash
#take the line indicated as the input parameter
#input_list.txt has the name of all the files to be processed
file=`sed -n "$1 p" input_list.txt`

command options $file

