#!/bin/bash

#for i in $(seq -f "%02g" 1 9); do
#  mkdir $i
#done

year=2017
for entry in *.zip; do
  for i in $(seq -f "%02g" 1 12); do
    if [[ $entry = *$year$i* ]]; then	
      mv $entry "$i"/
      break
    fi
  done
done
