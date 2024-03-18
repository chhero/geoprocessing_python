
**Since the guide for the Geoprocessing With Python is Kinda depreciated**

We will be utilizing geopandas as a gdal handler instead of the original _ospybook_ module
that came through with the book. 

Be sure to do this before starting or running the file
## Pre-requisite imports use this since the module for ospybook ##
## is depreciated all of the codes produces an error without exception ##
## as per dubugging the module ill be uploading updated module for this coursecode ##

import os #be sure to import this if using vs to access files
import sys
from osgeo import ogr 
import geopandas as gpd
import matplotlib.pyplot as plt

## <-- END --> ##

###### FILES DIRECTORY #####

data_dir = r'replace_with_your_own_path'
data_path_global = r"replace_with_your_own_path"
# Set the path to your shapefile
world = gpd.read_file(data_path_global)

##### END #####


