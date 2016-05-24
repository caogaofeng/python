import numpy as np
from numpy import *


data = np.loadtxt("sal.txt").T
print type(data)
print data

datain = data[:-1,:] 
dataout = data[1:,:]

print'11111111111'
print datain
print'22222222222222'
print dataout

x = array([1, 2, 3])

print matrix(x).T