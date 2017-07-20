#!/bin/bash

# Variables to change
codec="h264"
ext=".mp4"

# Setup
LOG="${0}.log"

if [ -f $LOG ] ; then
    rm $LOG
fi

#Script
while IFS='' read -r line || [[ -n "$line" ]] ; do
    echo "File: ${line}" >> $LOG
    if [ "$codec_file" == "$codec" -a ${line: -4} == $ext ] ;
    then
        cp $line "${line}.h264.mp4"
    else
        codec_file=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 $line)
        time -p "ffmpeg -i $line -f mp4 -c:v libx264 -c:a copy -crf 17 "${line}.h264.mp4" < /dev/null" 2>>$LOG
        echo "" >> $LOG
    fi
done < "video_files.txt"
