#!/bin/bash

find ./ -type f -name "*.h264.mp4" -execdir bash -c 'ffmpeg -y  -i "{}" -ss 3 -vframes 1 "{}.jpg"' \;
