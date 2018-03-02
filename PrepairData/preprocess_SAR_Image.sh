#!/bin/bash

year=2017
for month in $(seq -f "%02g" 1 12); do
  cd $month
  echo $PWD

  unzip -q \*.zip

  i=0
  for entry in *.SAFE; do
    python ../PrepairData/preprocess_SAR_Image.py $entry $i  
    let i=i+1
  done
  
  python ../PrepairData/merge.py $month $year
  cd ../Data2
  python ../PrepairData/resample.py $month $year
  
  cd ..
done
