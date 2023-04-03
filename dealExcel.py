# coding:utf-8
import numpy

# 读取桌面的csv文件
filename = 'C:\\Users\\Qbss\\Desktop\\Data.csv'

fn = open(filename, 'r', encoding='utf-8')

# 将csv读取为二维数组
loadtxt = numpy.loadtxt(fn, dtype=str, delimiter=',')

# 数组的行数
row = loadtxt.shape[0]

# 数组的列数
col = loadtxt.shape[1]

print(row)
print(col)
row_ = row / 49
print(row_)

# 按照每页49行，每行5列的格式，将数据写入到excel中
reshape = loadtxt.reshape(int(row_), 49, 9)

# 按照row_开始循环
for i in range(int(row_)):
    i_ = reshape[i]
    i__ = i_[0:]
    print(i__)  # 打印每页的数据


# print(reshape[1][0])
