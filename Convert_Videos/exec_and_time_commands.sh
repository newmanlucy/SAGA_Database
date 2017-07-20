#!/bin/bash
LOG="${0}.log"

if [ -f $LOG ] ; then
    rm $LOG
fi

while IFS='' read -r line || [[ -n "$line" ]] ; do
    echo "Command: ${line}" >> $LOG
    time -p "${line}" 2>>$LOG
    echo "" >> $LOG
done < "commands.txt"
