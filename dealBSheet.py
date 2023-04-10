import math

import numpy
import pandas

filename = 'sheet.xlsx'

fn = open(filename, 'r', encoding='utf-8')

excel = pandas.read_excel(filename, sheet_name=None, header=None)

b_excel = excel['B']

loadtxt = b_excel.to_numpy()

# 最大需求量
max_demand = loadtxt[0][1]

# 变压器最大容量
max_capacity = loadtxt[1][1]

nan = loadtxt[0][3]

# 取最大需求量和变压器最大容量中最大值
max_value = max(max_demand, max_capacity)



# 如果max_value不是数字，抛出异常
if not isinstance(max_value, (int, float)):
    raise Exception('max_value is NaN')

# 取loadtxt的第四行到最后一行
loadtxt_ = loadtxt[3:]

# 用一个树字典存储loadtxt_的值
group = {}

# 循环loadtxt_的每一行,按照第一列的值进行分组
for i in range(len(loadtxt_)):
    # 取loadtxt_的第i行
    i_ = loadtxt_[i]
    # 取loadtxt_的第i行的第一列
    i__ = i_[0]
    # 如果第四列为nan或者0，将第四列的值置为差值与2的最小值
    if math.isnan(i_[3]) or i_[3] == 0:
        i_[3] = min(i_[2] - i_[1], 2)
    # 判断数据的正确性，保证第四列的时长时必须小于等于第三列减去第二列的值
    elif i_[3] > i_[2] - i_[1]:
        i_[3] = i_[2] - i_[1]
    # 如果i__不在group中，将i__作为key，i_作为新的二维数组存入group中
    if i__ not in group:
        group[i__] = numpy.array([i_])
    # 如果i__在group中，将i_的值添加到group[i__]中
    else:
        group[i__] = numpy.vstack((group[i__], i_))

# 取group的第一个值
group_ = group['谷']
group__ = group['锋']
group___ = group['平']

if len(group_) == 1:
    group_ = numpy.vstack((group_, group___[0]))
elif len(group_) > 2:
    # 如果group_的长度大于2，取group__的前两行
    group_ = group_[0:2]

# 定义一个二维数组，用来存储group_的值
group_1 = numpy.array((group_[0][1], group_[0][1] + group_[0][3]))

# 如果group__的长度为1，只提供一次充放电循环
if len(group__) == 1:
    # 如果group_的长度为1，只提供一次充放电循环
    group_1 = numpy.vstack((group_1, numpy.array((group__[0][1], group__[0][1] + group__[0][3]))))
else:
    # 如果group__的长度大于1，提供两次充放电循环
    group_1 = numpy.vstack((group_1, numpy.array((group__[0][1], group__[0][1] + group__[0][3]))))
    group_1 = numpy.vstack((group_1, numpy.array((group_[1][1], group_[1][1] + group_[1][3]))))
    group_1 = numpy.vstack((group_1, numpy.array((group__[1][1], group__[1][1] + group__[1][3]))))

print(group_1)
