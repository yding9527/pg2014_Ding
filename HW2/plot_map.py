#2014-10-13 Yifeng Ding
#
#Write a script using this function to make
#a pcolormesh map of the topo/bathy
#

import numpy as np
import matplotlib.pyplot as plt
import urllib

url = "http://www.nio.org/userfiles/file/datainfo/global_merged5.txt"

f=urllib.urlopen(url)

lon=[]
lat=[]
top=[]

for line in f.readlines():
	if len(line)==4 :
		ilon,ilat,itop,dum = line.split()
		lon.append(ilon)
		lat.append(ilat)
		top.append(itop)

mlon=np.reshape(np.array(lon),[2161,4321])
mlat=np.reshape(np.array(lat),[2161,4321])
mtop=np.reshape(np.array(top),[2161,4321])

plt.pcolormesh(mlon,mlat,mtop,cmap=plt.cm.RdBu_r)

CS = plt.contour(mlon, mlat, mtop,(-1000.,1000),colors='k',linewidths=1)
CS.collections[1].set_linestyle('solid')

CS2 = plt.contour(mlon, mlat, mtop,(0.,),colors='k',linewidths=2)
CS2.collections[0].set_linestyle('solid')

plt.show()
