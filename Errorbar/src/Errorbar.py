# -*- coding:utf-8 -*-

# 标准偏差（Standard Deviation）
# 标准误差（Standard Error）
# 置信区间（Confidence Intervals）

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import t

# 在5-15范围内生成15个随机数据点
X = np.random.randint(5, 15, 15)

# 样本大小
n = X.size

# 平均
X_mean = np.mean(X)

# standard deviation 标准偏差
X_std = np.std(X)

# standard error 标准误差
X_se = X_std / np.sqrt(n)
# alternatively:
#    from scipy import stats
#    stats.sem(X)

# 95% Confidence Interval

dof = n - 1         # degrees of freedom
alpha = 1.0 - 0.95
conf_interval = t.ppf(1-alpha/2., dof) * X_std*np.sqrt(1.+1./n)

fig = plt.gca()
plt.errorbar(1, X_mean, yerr=X_std, fmt='-o')
plt.errorbar(2, X_mean, yerr=X_se, fmt='-o')
plt.errorbar(3, X_mean, yerr=conf_interval, fmt='-o')

plt.xlim([0,4])
plt.ylim(X_mean-conf_interval-2, X_mean+conf_interval+2)

# axis formatting
fig.axes.get_xaxis().set_visible(False)
fig.spines["top"].set_visible(False)
fig.spines["right"].set_visible(False)
plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="on", right="off", labelleft="on")

plt.legend(['Standard Deviation', 'Standard Error', 'Confidence Interval'],
           loc='upper left',
           numpoints=1,
           fancybox=True)

plt.ylabel('random variable')
plt.title('15 random values in the range 5-15')

plt.show()