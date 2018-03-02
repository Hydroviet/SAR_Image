def resample(imgDir):
    import math
    from snappy import jpy
    from snappy import ProductIO
    from snappy import GPF
    from snappy import HashMap
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    HashMap = jpy.get_type('java.util.HashMap')

    p = ProductIO.readProduct(imgDir)
    firstBand = p.getBands()[0]
    width = firstBand.getRasterWidth()
    height = firstBand.getRasterHeight()
    ratio = width/height

    parameters = HashMap()
    parameters.put('targetHeight', 1000)
    parameters.put('targetWidth', math.ceil(1000*ratio))
    product = GPF.createProduct('Resample', parameters, p)

    sourceName = imgDir.split('/')[-1]
    targetDir = '../DataResampled/' + sourceName
    ProductIO.writeProduct(product, targetDir, 'GeoTiff')
    return targetDir

if __name__ == '__main__':
    import sys
    month = sys.argv[1]
    year = sys.argv[2]
    print('resampling...')
    resample(year + month + '.tif')
    print('done')

