#!/bin/bash

# get year, language, day(s), and test flag from the terminal input
year=$1
language=$2
days=$3
test_flag=$4

path="./AdventOfCode$year/main.py"

if [ "$language" == "-p" ]; then
  python3 $path $days $test_flag
fi