#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do 
    ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 "$line"
done < "$1"
