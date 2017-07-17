#!/bin/bash
while IFS= read -r line
do
	echo "$line"
	ls "$line"
done < "video_paths.tsv"
