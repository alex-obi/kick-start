#!/bin/bash
FILE=$1
INPUT=$2
O=${FILE%%.*}.o
g++ -g -Wall -Wextra -pedantic-errors $FILE -o $O
cat $INPUT | ./$O
