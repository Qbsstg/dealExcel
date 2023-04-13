import numpy
import pandas

filename = 'train2 - 副本.xlsx'
excel = pandas.read_excel(filename, sheet_name=None, header=None)

a_to_numpy = excel['A'].to_numpy()

# 取第二行第二列开始的数据
a_to_numpy_ = a_to_numpy[1:, 1:]

# 定义一个二维数组
a_to_numpy__ = numpy.array([])

# 循环取出每一行的数据,判断数据的类型
for i in a_to_numpy_:
    # 如果出现‘-’，则将从‘-’开始的数据删除
    if '-' in i:
        i_ = i[0:i.tolist().index('-')]
        if len(a_to_numpy__) == 0:
            a_to_numpy__ = numpy.array([i_])
        else:
            a_to_numpy__ = numpy.vstack((a_to_numpy__, i_))
    else:
        if len(a_to_numpy__) == 0:
            a_to_numpy__ = numpy.array([i])
        else:
            a_to_numpy__ = numpy.vstack((a_to_numpy__, i))

print(a_to_numpy__)
