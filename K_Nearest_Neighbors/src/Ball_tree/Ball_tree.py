# -*- coding:utf-8 -*-

#测试 BallTree
from sklearn.neighbors import BallTree
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
bt = BallTree(X, leaf_size=30, metric="euclidean")
print bt.query(X, k=2, return_distance=False)