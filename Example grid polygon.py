import geopandas as gpd
 from shapely.geometry import Polygon
 import numpy as np
 points = gpd.read_file('points.shp')
 xmin,ymin,xmax,ymax =  points.total_bounds

 width = 2000
 height = 1000

 rows = int(np.ceil((ymax-ymin) /  height))
 cols = int(np.ceil((xmax-xmin) / width))

 Xleftorigin = xmin
 Xrightorigin = xmin + width
 Ytoprigin = ymax
 Ybottomrigin = ymax- height
 
 polygons = []
 for i in range(cols):
    Ytop = YtopOrigin
    Ybottom =YbottomOrigin
    for j in range(rows):
        polygons.append(Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])) 
        Ytop = Ytop - gridHeight
        Ybottom = Ybottom - gridHeight
    XleftOrigin = XleftOrigin + gridWidth
    XrightOrigin = XrightOrigin + gridWidth

grid = gpd.GeoDataFrame({'geometry':polygons})
grid.to_file("grid.shp")

## Reference
## https://gis.stackexchange.com/questions/269243/create-a-polygon-grid-using-with-geopandas
## This was an answer found on Stack Overflow.
