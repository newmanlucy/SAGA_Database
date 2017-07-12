#!/bin/bash
while IFS='' read -r line ; do
    echo "File: ${line}"
    ffprobe ${line}
    ffmpeg -i $line -f webm -c:v libvpx-vp9 -c:a libvorbis -ss 00:01:00 -t 00:00:02 -vf scale=-1:480 -b:v 500k "${line}_avgbr_500k.webm" < /dev/null
done < "list_files_here.txt"
