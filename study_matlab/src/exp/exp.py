# -*- coding:utf-8 -*-

from numpy import *
from matplotlib.figure import Figure
import matplotlib.pyplot  as plt

x = arange(1, 11)
print x[1]
# y = array([0.3243, 0.3433, 0.3623, 0.3813, 0.4003, 0.4320, 0.4127, 0.3934, 0.3741, 0.3548, 0.3355])
#y = array([0.43833128, 0.45731986, 0.47630844, 0.495297, 0.514, 0.5285417, 0.5092648, 0.4899583, 0.47065163, 0.45134506, 0.4320384])
y = (1 / (1 + exp(-x))) 
# 使用matplotlib画点
fig, ax = plt.subplots()
ax.plot(x, y, 'r*-', )
ax.set_ylim([0.7, 1])
ax.grid(color = 'b',alpha = 0.5,  linestyle = 'dashed', linewidth = 0.5 )
# plt.xscale()

# 显示
plt.show()
