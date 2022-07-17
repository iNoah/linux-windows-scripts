#!/bin/bash

unfiltered="$1"
known_words="$2"

cat $known_words | sort | uniq > temp1
egrep -w -o -i "[a-z]+{2,}" $unfiltered | tr '[:upper:]' '[:lower:]' | sort | uniq  > temp2

comm -23 temp2 temp1 > new_words.txt
rm temp1 temp2