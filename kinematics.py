#!/usr/bin/env python

import pandas as pd
import numpy as np


def integral(t,a_t):
	"""takes input arrays of x and f(x), returns the integral of f(x), using the
	Trapezoid rule implemented as difference equations."""
	v = np.zeros_like(a_t)
	v[0] = a_t[0]
	for i in range(1,len(a_t)):
		v[i] = v[i-1] + 0.5*(t[i] - t[i-1])*(a_t[i-1] + a_t[i])
	return t, v

