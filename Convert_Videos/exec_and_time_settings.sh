#!/bin/bash
LOG="${0}.log"

if [ -f $LOG ] ; then
    rm $LOG
fi

while IFS='' read -r lineF; do
    echo "File: ${lineF}" >> $LOG
    while IFS='' read -r lineC && read -r lineS <&3; do
        echo "Command: ${lineC}" >> $LOG
        echo "Settings: ${lineS}" >> $LOG
        #time -p "${lineC}" #2>>$LOG
        echo "" #>> $LOG
    done < "commands.txt" 3<"settings.txt"
done < "list_files_here.txt"
