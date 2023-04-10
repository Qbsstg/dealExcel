import math
import time
import warnings

import numpy
import pandas
from scipy import integrate


# 定义一个带返回值的方法(双返回值)
def fun_charge(loadtxt):
    # 消纳比例
    c_ration = float(loadtxt[0][1])

    # 最大需求量
    max_demand = loadtxt[1][1]

    # 变压器最大容量
    max_capacity = loadtxt[2][1]

    # 取最大需求量和变压器最大容量中最大值
    max_value = max(max_demand, max_capacity)

    # 如果max_value不是数字，抛出异常
    if not isinstance(max_value, (int, float)):
        raise Exception('max_value is NaN')

    # 取loadtxt的第四行到最后一行
    loadtxt_ = loadtxt[4:]

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

    return group_1, max_value, c_ration


def fun_y(loadtxt):
    row = loadtxt.shape[0]

    col = loadtxt.shape[1]

    time = loadtxt[0][0]

    loadtxt_ = loadtxt[0:, 1:]
    loadtxt__ = loadtxt_[1::4]

    # 定义一个一维数组
    loadtxt___ = numpy.array([])

    # 循环loadtxt__的每一行
    for i in range(len(loadtxt__)):
        for j in range(len(loadtxt__[i])):
            if math.isnan(loadtxt__[i][j]):
                continue
            loadtxt___ = numpy.append(loadtxt___, loadtxt__[i][j])

    x = numpy.arange(0, len(loadtxt___), 1)

    warnings.simplefilter('ignore', numpy.RankWarning)
    z1 = numpy.polyfit(x, loadtxt___, 20)
    p1 = numpy.poly1d(z1)

    return p1


def fun_oneSheet(loadtxt, excel_func, value_max):
    # 定义一个数组
    re = []

    #  循环charge_excel的每一行
    for j in range(len(excel_func)):
        # 取charge_excel的第i行
        j_ = excel_func[j]
        # 取charge_excel的第i行的第一列
        j__ = j_[0]
        # 取charge_excel的第i行的第二列
        j___ = j_[1]
        # 通过f_excel计算积分
        v, quad = integrate.quad(loadtxt, j__, j___)
        # 将积分的值添加到result中
        re.append(value_max * (j___ - j__) - v)

    return re


# 执行函数
if __name__ == '__main__':
    # 开始时间
    start = time.time()

    filename = 'train.xlsx'
    fn = open(filename, 'r', encoding='utf-8')
    excel = pandas.read_excel(filename, sheet_name=None, header=None)

    a_to_numpy = excel['A'].to_numpy()

    # 数组的行数
    row = a_to_numpy.shape[0]

    # 数组的列数
    col = a_to_numpy.shape[1]

    # 定义一个空的数组
    reshape = numpy.array([])

    # 判断数据的正确性
    if row % 49 == 0:
        reshape = a_to_numpy.reshape(int(row / 49), 49, 9)
    else:
        reshape = numpy.array([a_to_numpy])

    charge_excel, maxvalue, cration = fun_charge(excel['B'].to_numpy())

    # 定义一个二维数组，用来存储fun_oneSheet的返回值
    result = numpy.array([])
    print('页数' + len(reshape).__str__())

    # 循环reshape的每一行
    for a in range(len(reshape)):
        f_excel = fun_y(reshape[a])
        # 将fun_oneSheet的返回值添加到result中
        sheet = fun_oneSheet(f_excel, charge_excel, maxvalue)
        if len(result) == 0:
            result = numpy.array([sheet])
        else:
            result = numpy.vstack((result, sheet))

    # 将result 的值写入到excel中
    # pandas.DataFrame(result).to_excel('data.xlsx')

    print(result)

    # 取result每一行的最小值
    result = numpy.min(result, axis=1)
    # 对result进行倒序排序
    result = numpy.sort(result)[::-1]

    # 取result的长度
    result_len = len(result)

    # 按照消纳比例取result的值
    result = result[int(result_len * cration)]

    print(result)

    # 将c输出到result.txt中
    with open('result.txt', 'w') as f:
        f.write(result.__str__())
        f.close()

    # 结束时间
    end = time.time()
    print('耗时：' + (end - start).__str__())
