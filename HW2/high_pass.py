# Yifeng Ding
# 2014-10-06
#
# Create a 'high-pass' filter function that removes a trend from a give series of points using a polynomial fit of order N.
#

import numpy as np
import matplotlib.pyplot as plt

def high_pass(X,Y,rank=1):
	psol = np.polynomial.Polynomial.fit(X, Y, rank)

	diff = Y-psol(X)

	return diff