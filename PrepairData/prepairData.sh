#!/bin/bash

#for i in $(seq -f "%02g" 1 9); do
#  mkdir $i
#done

year=2017
for entry in *.zip; do
  for i in $(seq -f "%02g" 1 12); do
    if [[ $entry = *$year$i* ]]; then	
      if [[ ! -d "$i" ]]; then
        mkdir "$i"
      fi
      mv $entry "$i"/
      break
    fi
  done
done

for month in $(seq -f "%02g" 1 12); do
  if [[ -d "$month" ]]; then
    cd $month
    echo $PWD

    # Check if zip file is unzipped or not. If not unzipped yet, unzip it
    for zipfile in *.zip; do
      echo $zipfile
      zipfileName=${zipfile%%.zip}
      if [[ ! -d "${zipfileName}.SAFE" ]]; then
        unzip -q $zipfile
      else
        echo "Zip file has been already unzipped"
      fi
    done

    cd ..
  fi
done
