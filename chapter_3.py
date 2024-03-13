
######## Git Guide Clemente - Geomatics #########

#Requirements 
#Python Environment - gdal - osgeo - ospybook - data-source (anaconda / jupyter - optional)

#### Links #####

#Installing Python and Environment
# 1. https://phoenixnap.com/kb/how-to-install-python-3-windows\
# Follow all the instructions be sure na it path asya na para ha environment ma activate
# 2. Install Libraries

pip install gdal
pip install osgeo
pip install numpy
pip install matplotlib
pip install pyproj

#3. Download an osgeopy-data iclick la iton na download button mazip na iton 900+mb 
# Link: https://app.box.com/s/1cwdnolsmtf0s04o0hshbv4vxiuqcmi9

#Directory format

#Folders 
C:\NameofUser
  -Desktop
    --Geomatics
        ---osgeopy-data
          ----> [Files han Zip
        ---ospybook
        ---output
                 
#Installing of ospybook - run la an setup tas fdiretso na import

##### Number 1 & 2 #####

#Set up anay inin kay importante inin ha next numbers#
import os
import sys
data_dir = r'C:\filepath'
# data_dir = makukuha mo inin hiya hadto na zip na gindownload na data source bali just extract the file then
# then an extracted na folder amo an gagamiton for example ha desktop la ginexport/ginextract
# "C:\Users\[name han iyo laptop]\Desktop\osgeopy-data"

#Start number 1

from osgeo import ogr

# Get the number of supported drivers
count = ogr.GetDriverCount()

# Get and print the names of all drivers
for i in range(count):
    driver = ogr.GetDriver(i)
    driver_name = driver.GetName()
    print(driver_name)
  
#end

###### Number 3 & 4 ######

#Hongkong number 3

# Open the data source for the examples.
#CODE SNIPPET
fn = os.path.join(data_dir, 'global', 'ne_50m_populated_places.shp')
ds = ogr.Open(fn, 0)
if ds is None:
    sys.exit('Could not open {0}.'.format(fn))
lyr = ds.GetLayer(0)

# Get the total number of features and the last one.
num_features = lyr.GetFeatureCount()
last_feature = lyr.GetFeature(num_features - 1)
print(last_feature.NAME)
#END OF CODE SNIPPET

#Dapat it answer hongkong syakni ak if may error tas isend usually ma error la iton 
#basta di naka indicate an iyo directory

####### Number 5 ######










