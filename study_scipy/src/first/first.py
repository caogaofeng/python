# -*- coding:utf-8 -*-
from numpy import * 

from numpy.random import *
from scipy.integrate import quad, dblquad, tplquad
from scipy.linalg import solve
from scipy.linalg.misc import norm
from matplotlib.pyplot import subplots
from scipy import optimize


# quad单积分 dblquad 双重积分 tplquad 三重积分
def f(x):
    return x ** 2
val = quad(f, 0, 1)
print val
print type(val)

# Ax = b A是矩阵 x b 是向量
A = array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
b = array([1, 2, 3])
x = solve(A, b)
print x

print dot(A, x)
print Inf + 1

# 打印矩阵A的2范数
print norm(A, ord=2)

def y(x):
    return 4*x**3 + (x - 2)**2 + x**4

fig, ax = subplots()
print fig, ax
x = linspace(-5, 3, 100)
ax.plot(x, y(x))
# fig.show()
# raw_input()

x_min = optimize.fmin_bfgs(y)
print x_min
print y(-3)

