# Yifeng Ding
# 2014-10-06
#
# Calculate the distance between each of the points in two arrays.

import numpy as np
from numpy import sqrt

def dis_mtrx(m,n):
  if m.shape[1] is 2 and n.shape[1] is 2:

    xs0, ys0 = np.meshgrid(m[:,0],n[:,0])
    xs1, ys1 = np.meshgrid(m[:,1],n[:,1])
    result = sqrt((xs1-ys1)**2 + (xs0-ys0)**2)
    return result

  else:
    print "Arrays dimensions problem need to be fixed..."
