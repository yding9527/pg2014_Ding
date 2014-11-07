# 2014-11-04
# Shallow Water Model
# Yifeng Ding

def shallow_wat(n_time,n_pts,H,dx,dt):
	import numpy as np
	import matplotlib.pyplot as plt
	import time
	import pylab

	g=9.8

	t=np.array(range(0,n_time))
	x=np.array(range(0,n_pts))
	eta=np.array(np.zeros([n_pts,n_time]))
	u  =np.array(np.zeros([n_pts+1,n_time]))
	eta[n_pts/2.,0]=H/2.


	T,X=np.meshgrid(t,x)
	print eta[:,0]

	for i in range(1,n_time):
		u[1:-1,i] = u[1:-1,i] - g*dt/dx*(eta[1:,i-1]-eta[:-1,i-1])
		eta[:,i] = eta[:,i] - H*dt/dx*(u[1:,i]-u[:-1,i])
		print i
		print u[:,i]
	#	print eta[:,i]
	#	time.sleep(2.5)

	for nn in range(n_time):
		plt.clf();plt.plot(eta[:,nn]);
		pylab.ylim([-6,6])
		plt.savefig('./frames/frame_%04d.png' % nn)


	return X,T,eta
  
import matplotlib.pyplot as plt  
X,T,eta=shallow_wat(n_time=100,n_pts=21,H=10.,dx=100.,dt=5.0)
