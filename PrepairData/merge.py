import rasterio
from rasterio.merge import merge
import numpy as np

def mergeGeotiff(month, year):
    yearLabel = str(year)
    monthLabel = str(month).zfill(2)
    ds1 = rasterio.open('1.tif')
    ds2 = rasterio.open('2.tif')
    a = ds1.read()
    b = ds2.read()
    
    dest, outTransform = merge([ds1, ds2])
    profile = ds1.profile
    profile['transform'] = outTransform
    profile['height'] = dest.shape[1]
    profile['width'] = dest.shape[2]
    
    dstDir = '../DataMerged/' + yearLabel + monthLabel
    with rasterio.open(dstDir + '.tif', 'w', **profile) as dst:
        dst.write(dest)
    return dstDir

if __name__ == '__main__':
    import sys
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    print('merging...')
    mergeDir = mergeGeotiff(month, year)
    print('done')


