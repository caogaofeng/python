# coding=utf-8
from numpy import *
from scipy import rand

A = rand(5,5)
print A

m, n = A.shape
B = A.reshape(25,1)
print B

C = A.flatten("C")
print C
print type(C)

D, G = mgrid[0:5, 0:5]
F = mgrid[0:5]
print F
print F.shape
print D, G
print D.shape
print D[1][1]
print type(D)
print type(eye(4))