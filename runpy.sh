#!/bin/bash
FILE=$1
INPUT=$2
timestamp=$(date +%Y%m%d-%H%M%S)
cat $INPUT | python $FILE
