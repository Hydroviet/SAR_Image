from snappy import jpy
from snappy import ProductIO
from snappy import GPF
from snappy import HashMap

def subset(product, borderRectInGeoCoor):
    from snappy import GPF
    from snappy import HashMap
    from snappy import jpy
    import snappy

    xmin = borderRectInGeoCoor[0]
    ymin = borderRectInGeoCoor[1]
    xmax = borderRectInGeoCoor[2]
    ymax = borderRectInGeoCoor[3]

    p1 = '%s %s' %(xmin, ymin)
    p2 = '%s %s' %(xmin, ymax)
    p3 = '%s %s' %(xmax, ymax)
    p4 = '%s %s' %(xmax, ymin)
    wkt = "POLYGON((%s, %s, %s, %s, %s))" %(p1, p2, p3, p4, p1)
    WKTReader = snappy.jpy.get_type('com.vividsolutions.jts.io.WKTReader')
    geom = WKTReader().read(wkt)

    HashMap = jpy.get_type('java.util.HashMap')    
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()

    parameters = HashMap()
    parameters.put('copyMetadata', True)
    parameters.put('geoRegion', geom)
    parameters.put('outputImageScaleInDb', False)
    subset = GPF.createProduct('Subset', parameters, product)
    return subset

def calibrate(product):
    from snappy import GPF
    from snappy import HashMap
    
    parameters = HashMap() 
    parameters.put('outputSigmaBand', True) 
    parameters.put('outputImageScaleInDb', False)  
    Calibrate = GPF.createProduct('Calibration', parameters, product)
    return Calibrate

def terrainCorrection(product):
    from snappy import GPF
    from snappy import HashMap
    parameters = HashMap()

    parameters.put('demResamplingMethod', 'NEAREST_NEIGHBOUR') 
    parameters.put('imgResamplingMethod', 'NEAREST_NEIGHBOUR') 
    parameters.put('demName', 'SRTM 3Sec') 
    parameters.put('pixelSpacingInMeter', 10.0) 

    terrain = GPF.createProduct('Terrain-Correction', parameters, product)
    return terrain

def speckleFilter(product):
    from snappy import GPF
    from snappy import HashMap
    parameters = HashMap()

    parameters.put('filter', 'Lee')
    parameters.put('filterSizeX', 5)
    parameters.put('filterSizeY', 5)
    parameters.put('dampingFactor', 2)
    parameters.put('edgeThreshold', 5000.0)
    parameters.put('estimateENL', True)
    parameters.put('enl', 1.0)

    Speckle = GPF.createProduct('Speckle-Filter', parameters, product)
    return Speckle

def preprocess_SAR_Image(s1path, borderRectInGeoCoor = None, i = None):
    from snappy import ProductIO
    s1meta = "manifest.safe"
    s1product = "%s/%s" % (s1path, s1meta)
    reader = ProductIO.getProductReader("SENTINEL-1")
    product = reader.readProductNodes(s1product, None)
    parameters = HashMap()
    
    print('Subset', end = ' ')
    if borderRectInGeoCoor != None:
        Subset = subset(product, borderRectInGeoCoor)
    else:
        Subset = product
    
    print('Calibrate', end = ' ')
    Calibrate = calibrate(Subset)
    
    print('Terrain', end = ' ')
    Terrain = terrainCorrection(Calibrate)
    TerrainDB = GPF.createProduct("LinearToFromdB", parameters, Terrain)
    
    print('SpeckleFilter', end = ' ')
    Speckle = speckleFilter(TerrainDB)
    
    print('WriteProduct')
    targetName = 'target'
    if i != None:
        targetName = str(i)
    ProductIO.writeProduct(Speckle, targetName, 'GeoTiff')
    
    del product, Subset, Calibrate, Terrain, TerrainDB, Speckle

def main():
    import os, sys
    img = sys.argv[1]
    i = int(sys.argv[2])
    borderRects = [[103.509, 12.803, 104.618, 13.304],
                   [103.976, 12.512, 104.984, 12.516]]
    preprocess_SAR_Image(img, borderRects[i], i + 1)

if __name__ == '__main__':
    main()
