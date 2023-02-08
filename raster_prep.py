#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:11:00 2023

@author: gopal
"""

import rasterio
import rasterio.features
import rasterio.warp
import rasterio.plot as rp
from matplotlib import pyplot as plt
import os
import numpy as np


proj_path = "/Users/gopal/Google Drive/_Research/Research projects/ML/download_gee_rasters/lahore_18km"
oli_path = os.path.join(proj_path,"oli8_lahore_18km_GEE")
s2_path = os.path.join(proj_path,"s2_lahore_18km_GEE")


oli_name = "LC08_149038_20160424.tif"
oli = rasterio.open(os.path.join(oli_path, oli_name))


oli.height
oli.width

# %%


# %%

oli.indexes
oli.dtypes

oli.bounds


# %%
s2_name = "20190126T055121_20190126T055823_T43RDQ.tif"
s2 = rasterio.open(os.path.join(s2_path, s2_name))

# %%
print('oli crs', oli.crs)
print('s2 crs', s2.crs)

# %%
s2.transform * (0, 0)
oli.transform * (0, 0)

# %%

oli.width * 30 + 

# %%
oli.bounds[0] + oli.width * 30

# %%

oli.transform

# %%
print('px 0,0 coords', oli.transform * (0, 0))
print('px 0,0 ul', oli.xy(0,0,offset = 'ul'))
print('px 0,0 center', oli.xy(0,0,offset = 'center'))
print('px 0,0 br', oli.xy(0,0,offset = 'lr'))
print('px 1,1 ul', oli.xy(1,1,offset = 'ul'))

# %%

# oli.transform * (222, 92)

# %%
oli.height


# %%

# im = oli.read([3, 2, 1])

rp.show((oli.read([3,2,1]) - 400 )/ 40000)


plt.imshow(im)

# %%


# arr[1].shape
# %%
def adj_bands(arr):
    for i in np.arange(arr.shape[0]):
        arr[i] = rp.adjust_band(arr[i])
    
    return arr

# %%

arr = oli.read([3,4,5])
rp.show(adj_bands(arr))

# %%

arrs2 = s2.read([4,3,2])
rp.show(adj_bands(arrs2))

# %%
oli.width
#

# with rasterio.open(os.path.join(oli_path, r_name)) as dataset:

#     # Read the dataset's valid data mask as a ndarray.
#     mask = dataset.dataset_mask()

#     # Extract feature shapes and values from the array.
#     for geom, val in rasterio.features.shapes(
#             mask, transform=dataset.transform):

#         # Transform shapes from the dataset's own coordinate
#         # reference system to CRS84 (EPSG:4326).
#         geom = rasterio.warp.transform_geom(
#             dataset.crs, 'EPSG:4326', geom, precision=6)

#         # Print GeoJSON shapes to stdout.
#         print(geom)