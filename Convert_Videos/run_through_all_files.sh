#!/bin/bash

# Variables to change
codec="h264"
ext=".mp4"

# Setup
LOG="${0}.log"
LOGTIME="${0}_time.log"

if [ -f $LOG ] ; then
    rm $LOG
fi

if [ -f $LOGTIME ] ; then
    rm $LOGTIME
fi

#Script
while IFS='' read -r line || [[ -n "$line" ]] ; do
    echo "File: ${line}" >> $LOGTIME
    filename="$(echo "${line}" | rev | cut -d"/" -f1 | rev)"
    if [ "$codec_file" == "$codec" -a ${line: -4} == $ext ] ;
    then
        cp $line "${line}.h264.mp4"
    else
        codec_file=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 $line)
        script() {
            ffmpeg -i $line -f mp4 -c:v libx264 -c:a copy -crf 17 "$filename.h264.mp4" < /dev/null
        }
        ( time -p script &>> $LOG ) 2>> $LOGTIME
        echo "" >> $LOGTIME
    fi
done < "video_files.txt"
