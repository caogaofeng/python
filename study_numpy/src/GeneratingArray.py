# coding=utf-8
from numpy import *
x, y = mgrid[0:5, 0:5]
print '矩阵x:'
print x
print '矩阵y:'
print y.T
v = array([1, 2, 3, 4])
M = array([[1, 2], [3, 4]])
n = array([[1], [2], [3]])
print type(n)
print '列矩阵：'
v1 = matrix(v).T
print v1
print type(v1)

print n
print v.shape
print n.shape

print v[0]
print M[1, 1]
print M[1][1]
print M[1]

print range(5)


which = [0, 0, 0, 0]
choices = [[1, 2, 3, 4], [5, 6, 7, 8]]
print choose(which, choices)


print arange(-1, 1, 0.1)

print '输出y的第一行元素：'
print y[0, :]

print '输出y的第一列元素：'
print '1111111111111111111111'
print y[:-2, :]

print '输出x * （y的第一列）'
print x * y[0, :]

print 'x * y: '
print x * y

print "dot(x, y)"
print dot(x, y)

print 'M的转置：'
print [[r[col] for r in M] for col in range(len(M[0]))]
print map(list, zip(*M))

print 'dot(v * v)'
print dot(v, v)


