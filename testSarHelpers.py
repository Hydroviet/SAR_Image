import sarHelpers
from time import time

start = time()
sarHelpers.preprocessSarFile(sarDownloadFilePath=['SARData/S1A_IW_GRDH_1SDV_20170221T225238_20170221T225303_015388_019405_9C41.SAFE',
                                                  'SARData/S1A_IW_GRDH_1SDV_20170221T225303_20170221T225328_015388_019405_0815.SAFE'],
                             geopandasDataFilePath='GeoData/mekongReservoirs',
                             geoDataIndex=0,
                             dstPath='GeoTiff/out.tif')
print('Execution time = %.3fs' % (time() - start))

'''
start = time()
sarHelpers.preprocessSarFile(sarDownloadFilePath='SARData/S1A_IW_GRDH_1SDV_20170221T225238_20170221T225303_015388_019405_9C41.SAFE',
                             geopandasDataFilePath='GeoData/mekongReservoirs',
                             geoDataIndex=0,
                             dstPath='GeoTiff1/out.tif')
print('Execution time = %.3fs' % (time() - start))
'''