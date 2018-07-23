#!/bin/bash

if [[ ! -d "DataMerged" ]]; then
  mkdir "DataMerged"
fi

if [[ ! -d "DataResampled" ]]; then
  mkdir "DataResampled"
fi

year=2017
for month in $(seq -f "%02g" 1 12); do
  if [[ -d "$month" ]]; then
    cd $month
    echo $PWD
    
    # Preprocess SAR image (Subset Calibrate Terrain SpeckleFilter WriteProduct)
    i=0
    for file in *.SAFE; do
      echo $file
      let j=i+1
      if [[ ! -f "$j.tif" ]]; then
        echo "Image not preprocessed"
        python ../PrepairData/preprocess_SAR_Image.py $file $i
      else
        echo "Image has been already preprocessed"
      fi  
      let i=j
    done
  
    # Merge two geotiff of Tonlesap
    if [[ ! -f "../DataMerged/$year$month.tif" ]]; then
      python ../PrepairData/merge.py $month $year
    else 
      echo "Images have been already merged"
    fi

    # Resample merged geotiff
    cd ../DataMerged
    if [[ ! -f "../DataResampled/$year$month.tif" ]]; then
      python ../PrepairData/resample.py $month $year
    else
      echo "Image has been already resampled"
    fi

    cd ..
  fi
done
