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
  helper_path="./AdventOfCode$year/helper.c"
  hashtable_path="./AdventOfCode$year/hashtable.c"
  gcc $path $helper_path $hashtable_path -o build/main

  # run c executable
  ./build/main
  rm ./build/main
fi