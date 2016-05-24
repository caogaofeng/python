# -*- coding: utf-8 -*-

# Python 2.7 学习参考脚本


# print 打印函数
print "Hello World!"




### import ###

# 导入数学模块
import math
math.sqrt(25)

# 导入一个函数
from math import sqrt
sqrt(25)  # 没必要再引用模块的名字了

# 一次导入多个函数
from math import cos, floor

# 引入模块中的所有函数(不建议)
from os import *

# 引入模块并起别名
import numpy as np

# 显示math模块下的所有函数
dir(math)




### 数据类型 ###

# 判断一个对象的类型
type(2)        # 返回 'int'
type(2.0)      # 返回 'float'
type('two')    # 返回 'str'
type(True)     # 返回 'bool'
type(None)     # 返回 'NoneType'

# 检查一个对象是什么类型
isinstance(2.0, int)   # 返回 False
isinstance(2.0, (int, float))  # 返回 True

# 转换数据类型
float(2)
int(2.9)
str(2.9)

# 0，None，和空容器转为False
bool(0)
bool(None)
bool('')   # 空字符串
bool([])   # 空列表(list)
bool({})   # 空字典(dictionary)

# 非空容器和非0转为True
bool(2)
bool('two')
bool([2])




### Math ###
10 + 4    # 加法(14)
10 - 4    # 减法(6)
10 * 4    # 乘法(40)
10 ** 4   # 指数(10000)
10 / 4    # 除法(2, 因为两个数同为int类型)
10 / float(4)  # 除法(2.5)
5 % 4     # 求余(1)

# 在python 2.x 中强制做"真除法"（在Python 3.x中没有必要）
# from __future__ import division  # 放在文件头
# print 10 / 4   # 返回 2.5
10 // 4          # 返回 2



### 比较和bool运算 ###
# 全部返回True
5 > 3
5 >= 3
5 != 3
5 == 5

# bool 运算 全部返回True
5 > 3 and 6 > 3
5> 3 or 5 < 3
not False
False or not False and True  # 运算顺序为：not，and，or




### 控制语句 ###

# if 语句
x = 3
if x > 0:
    print '正数'

# if/else 语句
if x > 0:
    print '正数'
else:
    print '<= 0'

# if/elif/else 语句
if x > 0:
    print '正数'
elif x == 0:
    print '0'
else:
    print '负数'

# if 语句，放在一行（不建议）
if x > 0: print '正数'
# if/else 语句，放在一行 (不建议)
print '正数' if x > 0 else '<= 0'




### 列表list ###

# 创建一个空list (两种方法)
empty_list = []
empty_list = list()

# 创建一个list
simpsons = ['homer', 'marge', 'bart']

# 获取list元素
simpsons[0]
len(simpsons)   # 返回list长度(3)

# 修改list  (操作不会返回list)
simpsons.append('lisa')   # 在list尾插入元素  也可以append一个list
simpsons.extend(['itchy', 'scratchy'])  # 在list尾插入多个元素
# simpsons.append(['itchy', 'scratchy'])  # 比较和extend的区别
simpsons.insert(0, 'maggie')     # 在0索引处插入元素（把所有东西向右移）
simpsons.remove('bart')          # 查找第一元素然后删除

simpsons.pop(0)                  # 删除索引为0的元素并返回
del simpsons[0]                  # 同上，但是不返回
simpsons[0] = 'krusty'             # 替换索引0的元素

#  用+号拼接list（比extend方法慢）
neighbors = simpsons + ['ned', 'rod', 'todd']  # simpsons 不变

# 在list中查找元素
simpsons.count('lisa')   # 计算元素的个数
simpsons.index('itchy')  # 返回第一元素的索引

# 分割list [开始：结束：跨步]
weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
weekdays[0]      # 'mon'
weekdays[0:3]    # 'mon', 'tues', 'wed'
weekdays[:3]     # 'mon', 'tues', 'wed'
weekdays[3:]     # 'thurs', 'fri'
weekdays[-1]     # 'fri' 最后一个元素
weekdays[::2]    # 0,2,4   'mon' 'wed' 'fri'
weekdays[::-1]   # 倒序 (4, 3, 2, 1, 0)  'fri' 'thurs' 'wed' 'tues' 'mon'

#倒序
list(reversed(weekdays))

# 在原地排序
simpsons.sort()
simpsons.sort(reverse=True)  # 倒序
simpsons.sort(key=len)       # 通过key排序


# 返回一个排过序的列表（不修改原始列表）
sorted(simpsons)
sorted(simpsons, reverse=True)
sorted(simpsons, key=len)

# 在排过序的列表中插入一个元素，并保持排序状态
num = [10, 20, 40, 50]
from bisect import insort
insort(num, 30)

# 创建同一个列表的引用
same_num = num
same_num[0] = 0      # 修改一个，same_sum 和 sum 一起改了

# copy 一个列表（两种方法）
new_num = num[:]
new_num = list(num)

# 比较列表list
id(num) == id(same_num) # True
id(num) == id(new_num)  # False
num is same_num         # True
num is new_num          # False
num == same_num         # True
num == new_num          # True (他们的内容相同)


### 元组（Tuple） ###
# 和list相似，但是它不能改变大小

# 创建一个元组
digits = (0, 1, 'two')  # 创建一个元组
digits = tuple([0, 1, 'two'])  # 从list创建元组
zero = (0,)         # 逗号是必不可少的，它指定zero是一个元组,没有的话就是数字0了

# 访问元组数据
digits[2]   # 返回'two'
len(digits) #      3
digits.count(0)  # 0的个数 （1）
digits.index(1)  # 返回第一个1的索引(1)

# 元组里的元素不能修改
# digits[2] = 2  # 抛出一个错误

# 拼接元组
digits = digits + (3, 4)

# 创建一个重复元素的元组（通常和list一起使用）
(3, 4) * 2   # 返回（3，4，3，4）

# 排序一个元组列表
tens = [(20,60), (10, 40), (20, 30)]
sorted(tens)   # 按元组里的第一个元素排序，第一个元素相同，比较第二个
               # [(10, 40), (20, 30), (20, 60)]

# 元组解包
bart = ('male', 10, 'simpson')
(sex, age, surname) = bart   # 一次符三个值





### 字符串 ###

#创建一个字符串
s = str(42)   # 把其它类型的数据转化为string
s = 'I like you'

# 提取string
s[0]    # 返回 'I'
len(s)  # 返回 10

# 分割字符串
s[:6]    # 'I like'
s[7:]    # 'you'
s[-1]    # 'u'

# 基本的string方法 （不修改原string）
s.lower()    # 'i like you'
s.upper()    # 'I LIKE YOU'
s.startswith('I')   # True
s.endswith('you')    # True
s.isdigit()         # False (Ture:数字组成的字符串)
s.find('like')      # 2 索引
s.find('hate')      # -1 没有找到
s.replace('lkie', 'love')  # 替换 'like' 为 'love'


# 分割字符串
s.split(' ')  # ['I','like','you']
s.split()     # 同上
s2 = 'a, an, the'
s2.split(',')   # ['a',' an',' the']

# 把列表中的字符串连成一个字符串
stooges = ['larry','curly','moe']
' '.join(stooges)     # 'larry curly moe'

# 连接字符串
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4
s3 + ' ' + str(42) # 'The meaning of life is 42'

#移除字符串前后中的空白字符
s5 = '  ham and cheese  '
s5.strip()    # 'ham and cheese'

# 字符串替换
'raining %s and %s' % ('cat', 'dogs')    # 老方法
'raining {} and {}'.format('cats', 'dogs') # 新方法
'raining {arg1} and {arg2}'.format(arg1='cats', arg2='dogs')

# 字符串格式化
'pi is {:.2f}'.format(3.14159)   # 'pi is 3.14'

# normal string 和 raw string
print 'first linensecond line'
print r'first linenfirst line'





###  字典（dictionaries） ###
# 由key-value对组成
# key是唯一的，可以是string，数字，元组
# values 可以是任何值

# 创建一个空字典（两种方法）
empty_dict = {}
empty_dict = dict()

# 创建一个字典（两种方法）
family = {'dad':'homer', 'mom':'marge', 'size':6}
family = dict(dad='homer', mom='marge', size=6)

# 把元组列表转化为字典
list_of_tuples = [('dad','homer'), ('mom','marge'), ('size', 6)]
family = dict(list_of_tuples)

# 获取字典元素
family['dad']   # 'homer'
len(family)     # 3
family.keys()   # ['dad', 'mom', 'size']
family.values() # ['homer', 'marge', 6]
family.items()  # [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
'mom' in family # Ture
'marge' in family # False (只判断key)

# 修改字典
family['cat'] = 'snowball'  # 增加一个新纪录
family['cat'] = 'snowball ii' # 编辑一个以存在的记录
del family['cat']         # 删除一个记录
family['kids'] = ['bart', 'lisa']  # 值可以是列表
family.pop('dad')          # 删除一个记录并返回值
family.update({'baby':'maggie', 'grandpa':'abe'}) # 增加多个记录

family['mom']   # 'marge'
family.get('mom') # 同上
#family['grandma']  # 抛出错误
family.get('grandma')  # 返回None
family.get('grandma', 'not found')  # 'not found'

family['kids'][0]   # 'bart'
family['kids'].remove('lisa')   # 移除'lisa'

# 用字典替换字符串
'youngest child is %(baby)s' % family   # 'youngest child is maggie'





### set  ###
# 无重复集合

# 创建空set
empty_set = set()

# 创建集合
languages = {'python', 'r', 'java'}
snakes = set(['cobra', 'viper', 'python'])

len(languages)  # 3
'python' in languages   # True

# set 操作
languages & snakes # 两个集合的交集  ｛'python'｝
languages | snakes # 联合   {'cobra', 'r', 'java', 'viper', 'python'}
languages - snakes # {'r', 'java'}
snakes - languages # {'cobra', 'viper'}

# 修改集合
languages.add('sql')   # 增加一个元素
languages.add('r')     # 试图增加一个以存在的元素，忽略，没有错误
languages.remove('java') # 移除一个元素
#languages.remove('c')    # 试图移除一个不存在的元素，抛出错误
languages.discard('c')   # 移除一个存在的元素，如果不存在，忽略
languages.pop()          # 移除并返回元素
languages.clear()        # 清空集合
languages.update('go', 'spark') # 增加多个元素

# 排序
sorted(set([9, 0, 2, 1, 0]))  # [0, 1, 2, 9]   去重排序






### 定义函数 ###

# 定义一个没有参数和返回值的函数
def print_text():
    print 'you are dumb'

# 调用一个函数
print_text()

# 定义一个有一个参数没有返回值的函数
def print_this(x):
    print x

# 调用
print_this(4)  # 4
n = print_this(4)  # 打印4，但是不会给n赋值

# 定义一个一个参数和返回值的函数
def square_this(x):
    return x ** 2

# 带函数描述
def square_this(x):
    """ Return the square of number."""
    return x ** 2

square_this(3)
var = square_this(3) # var = 9

# 带默认参数的函数
def calc(a, b, op='add'):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a -b
    else:
        print 'no op'

# 调用
calc(10, 4, op='add')   # 14
calc(10, 4, 'add')      # 14
calc(10, 4)             # 14
calc(10, 4, 'sub')      # 6
calc(10, 4, 'div')      # 'no op'


# 用 pass 写一个没有函数体的函数,它只是一个占位符
def stub():
    pass

# 一个函数返回2个值
def min_max(nums):
    return min(nums), max(nums)

nums = [1, 2, 3]
min_max_num = min_max(nums)  #  min_max_num = (1,3)  元组
min_num, max_num = min_max(nums) # min_num = 1,max_num = 3,  元组解包





### 匿名函数（Lambda）###

# 普通方式定义函数
def squared(x):
    return x ** 2

# lamba
squared = lambda x : x ** 2

# 通过最后的字符排列字符串（不用lambda）
simpsons = ['homer', 'marge', 'bart']
def last_letter(word):
    return word[-1]
sorted(simpsons, key=last_letter)
# 用lambda
sorted(simpsons, key=lambda word : word[-1])





### For 循环和 while循环

# range 返回整数列表
range(0, 3)   # [0, 1, 2]
range(3)      # 同上
range(0, 5, 2) # [0, 2, 4]  # 第三个参数跳跃

# for 循环（不建议)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print fruits[i].upper()

# 建议
for fruit in fruits:
    print fruit.upper()

# 用 xrange 避免遍历大数组时创建 整数数组
for i in xrange(10 ** 6):
    pass

# 用元组解包一次遍历两个东西
family = {'dad':'homer', 'mom':'marge', 'size':6}
for key, value in family.items():
    print key, value

# 用枚举 如果你想在循环中用索引
for index, fruit in enumerate(fruits):
    print index, fruit

# for/else 循环
for fruit in fruits:
    if fruit == 'banana':
        print "I like banana"
        break
else:    # 只用当代码没有执行break时
    print "Can't find the banana"

# while 循环
count = 0
while count < 5:
    print count
    count += 1

# 例子
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num ** 3)
# 等价 comprehension
cubes = [num**3 for num in nums]
# ---------------------------------
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)
# 等价 comprehension
cubes_of_even = [num**3 for num in nums if num % 2 == 0]
# ---------------------------------
cubes_add_squares = []
for num in nums:
    if num % 2 == 0:
        cubes_add_squares.append(num**3)
    else:
        cubes_add_squares.append(num**2)
# 等价 comprehension
cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]
# ---------------------------------
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)
# 等价 comprehension
items = [item for row in matrix
              for item in row]
# ---------------------------------
# set comprehension
fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}   # {5, 6}

# dictionary comprehension
fruit_lengths = {fruit:len(fruit) for fruit in fruits}              # {'apple': 5, 'banana': 6, 'cherry': 6}
fruit_indices = {fruit:index for index, fruit in enumerate(fruits)} # {'apple': 0, 'banana': 1, 'cherry': 2}




### map reduce  filter ###

# 'map'把一个操作应用到所有元素上
simpsons = ['homer', 'marge', 'bart']
map(len, simpsons)   # 求每个元素的长度 [5, 5, 4]
map(lambda word: word[-1], simpsons)  # ['r', 'e', 't']
# 等价
[len(word) for word in simpsons]
[word[-1] for word in simpsons]


# 先把前两个元素执行某个函数,求的结果，依次计算
reduce(lambda x,y: x + y, range(4)  # (((0+1)+2)+3) = 6

# 用指定函数过滤
filter(lambda x: x % 2 == 0, range(5))  # [0, 2, 4]