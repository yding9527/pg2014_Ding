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
	order_pos = np.where(diff > 0)
	order_neg = np.where(diff < 0)

	diff_pos = np.zeros(diff.shape)
	diff_neg = np.zeros(diff.shape)

	diff_pos[order_pos]=diff[order_pos]
	diff_neg[order_neg]=diff[order_neg]

	return diff_neg,diff_pos