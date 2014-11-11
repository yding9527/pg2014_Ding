# 2014-11-04
# Shallow Water Model
# Yifeng Ding


import numpy as np
import matplotlib.pyplot as plt
import time
import pylab

class shallow_wat(object):

	def __init__(self,n_time,n_pts,H,dx,dt):
		self.nt=n_time
		self.np=n_pts
		self.H =H
		self.dx=dx
		self.dt=dt

	def eta(self):
		g=9.8
		t=np.array(range(0,self.nt))
		x=np.array(range(0,self.np))
		eta=np.array(np.zeros([self.np,self.nt]))
		u  =np.array(np.zeros([self.np+1,self.nt]))
#		eta[self.np/2.,0]=self.H/2.
		eta[0,0]=self.H/2.


		T,X=np.meshgrid(t,x)

		for i in range(1,self.nt):
			u[1:-1,i] = u[1:-1,i] - g*self.dt/self.dx*(eta[1:,i-1]-eta[:-1,i-1])
			eta[:,i] = eta[:,i] - self.H*self.dt/self.dx*(u[1:,i]-u[:-1,i])

		for nn in range(self.nt):
			plt.clf();plt.plot(eta[:,nn]);
			pylab.ylim([-6,6])
			plt.savefig('./frames/frame_%04d.png' % nn)

		self.eta=eta
		self.X  =X
		self.T  =T

import matplotlib.pyplot as plt  
if __name__ == '__main__':
	data=shallow_wat(n_time=100,n_pts=21,H=10.,dx=100.,dt=5.0)
	data.eta()




