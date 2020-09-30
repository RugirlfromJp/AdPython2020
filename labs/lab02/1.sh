#!/usr/bin/bash

while true
do
    files=$(find /c/Users/masha/custom_tmp -maxdepth 1 -type f | wc -l)
    dirs=$(find /c/Users/masha/custom_tmp -maxdepth 1 -type d| wc -l)
    echo 'Contents of custom_tmp: ' $files ' files, ' $((dirs-1)) ' folders'
    sleep 10
done	