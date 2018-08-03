import sys
import sarHelpers

geopandasDataFilePath = sys.argv[1]
geoDataIndex = int(sys.argv[2])
dstPath = sys.argv[3]
sarDownloadFilePath = sys.argv[4]

filenamePrefix = dstPath[:-4]
rawImg = sarHelpers.getGeoTiffImage(sarDownloadFilePath=sarDownloadFilePath,
                                    geopandasDataFilePath=geopandasDataFilePath,
                                    geoDataIndex=geoDataIndex,
                                    dstPath=dstPath)
