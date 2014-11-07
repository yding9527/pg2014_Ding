# Yifeng Ding
# 2014-10-27
# in class demo

import numpy as np
import netCDF4
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# location of ssh data
data_url='http://apdrc.soest.hawaii.edu/dods/public_data/Model_output/HYCOM/hycom_hawaii_0.04_KPP'

# time index to plot
tidx = 10  # plot the most recent ssh field.

########################################

nc = netCDF4.Dataset(data_url)

lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]

m = Basemap(projection='lcc',
            llcrnrlon=np.min(lon), 
            urcrnrlon=np.max(lon), 
            llcrnrlat=np.min(lat), 
            urcrnrlat=np.max(lat),
            lat_0=np.mean(lat),
            lon_0=np.mean(lon),
            resolution='f')

x, y = m (*np.meshgrid(lon, lat))

ssh = nc.variables['ssh'][tidx, :, :]


# plot commands
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

m.fillcontinents()

pcm = ax.pcolormesh(x, y, ssh, cmap=plt.cm.RdBu_r) 
m.drawmeridians(np.arange(194, 210, 2),labels=[1,0,0,1])
m.drawparallels(np.arange(18, 26, 2),labels=[0,1,1,0])
cbar = plt.colorbar(pcm,orientation='horizontal',shrink=0.6)
cbar.set_label('Sea Surface Height(m)')

plt.title('HYCOM Regional Simulation with KPP\n')

plt.show()
