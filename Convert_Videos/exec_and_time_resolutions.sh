#!/bin/bash

# Variables to change
WIDTH=640
HEIGHT=480

# Setup
ASPRATIO=$(echo "$WIDTH/$HEIGHT" | bc -l)
SETWIDTH="$WIDTH:-1"
SETHEIGHT="-1:$HEIGHT"
SETRATIO=$SETWIDTH
SETASPRATIO=$ASPRATIO
LOG="${0}.log"

if [ -f $LOG ] ; then
    rm $LOG
fi

#Script
while IFS='' read -r lineF; do
    echo "File: ../${lineF}" >> $LOG
    eval $(ffprobe -v error -of flat=s=_ -select_streams v:0 -show_entries stream=height,width "../$lineF")
    if [ $(echo " $ASPRATIO > ${streams_stream_0_width}/${streams_stream_0_height}" | bc -l) = 0 ]; then
        SETRATIO=$SETWIDTH
    else
        SETRATIO=$SETHEIGHT
    fi
    while IFS='' read -r lineS; do
        echo "Settings: ${lineS}" >> $LOG
        #echo "ffmpeg -i ../${lineF} ${lineS} -vf scale=$SETRATIO \"../webm_video/${lineF}_HEY.webm\" < /dev/null" >> $LOG
        time -p "ffmpeg -i ../${lineF} ${lineS} -vf scale=$SETRATIO \"../webm_video/${lineF}_HEY.webm\" < /dev/null" 2>>$LOG
        echo "" >> $LOG
    done < "settings.txt"
done < "list_files_here.txt"


#done 3< "commands.txt" 4< "list_files_here.txt"
