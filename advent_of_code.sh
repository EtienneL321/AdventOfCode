#!/bin/bash

# get year, language, day(s), and test flag from the terminal input
year=$1
language=$2
days=$3
test_flag=$4



if [ "$language" == "-p" ]; then
  path="./AdventOfCode$year/main.py"
  python3 $path $days $test_flag

elif [ "$language" == "-c" ]; then
  path="./AdventOfCode$year/main.c"
  gcc $path -o main

  # run c executable
  ./main

  # remove c executable
  rm main
fi