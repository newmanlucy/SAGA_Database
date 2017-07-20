#!/bin/bash
{
    while IFS='' read -r line || [[ -n "$line" ]] ; do
#        echo "Text read from file: $line"
        eval $(ffprobe -v error -of flat=s=_ -select_streams v:0 -show_entries stream=height,width "$line")
        size=${streams_stream_0_width}x${streams_stream_0_height}
        echo $size
    done < "video_files.txt"
} | sort | uniq -c | sort -nr > video_res_sorted.txt

# while IFS='' read -r line || [[ -n "$line" ]]; do
