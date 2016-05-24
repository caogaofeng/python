# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

# 输入数据
mean_values = [1, 2, 3]
variance = [0.2, 0.4, 0.5]
bar_labels = ['bar 1', 'bar 2', 'bar 3']

fig = plt.gca()

# 画条
x_pos = list(range(len(bar_labels)))
plt.bar(x_pos, mean_values, yerr=variance, align='center', alpha=0.5)

# 设置y轴高度
max_y = max(zip(mean_values, variance)) # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])

# 标签和标题
plt.ylabel('variable y')
plt.xticks(x_pos, bar_labels)
plt.title('Bar plot with error bars')

# axis formatting
fig.axes.get_xaxis().set_visible(False)
fig.spines["top"].set_visible(False)
fig.spines["right"].set_visible(False)
plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="on", right="off", labelleft="on")

plt.show()