#!/usr/bin/env python

import pandas as pd
import numpy as np


def integral(t,a_t,v_0=0):
	"""takes input arrays of x and f(x), returns the integral of f(x), using 
	the Trapezoid rule implemented as difference equations."""
	v = np.zeros_like(a_t)
	v[0] = v_0
	for i in range(1,len(a_t)):
		v[i] = v[i-1] + 0.5*(t[i] - t[i-1])*(a_t[i] + a_t[i-1])
	return v

def zero(fx,x0,xf):
	"""Takes an array of data f(x), and an initial calibration period
	x0 to xf, and zeros the data set s.t. that first initial calibration
	period is centered around zero."""
	avg = np.sum(fx[x0:xf])/float(xf-x0)
	fxZero = fx - avg
	return fxZero

	