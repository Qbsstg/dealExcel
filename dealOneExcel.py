import numpy
from scipy import integrate
import pylab

# 读取桌面的csv文件
filename = 'C:\\Users\\Qbss\\Desktop\\test.csv'

fn = open(filename, 'r', encoding='utf-8')

# 将csv读取为二维数组
loadtxt = numpy.loadtxt(fn, dtype=str, delimiter=',')

# 数组的行数
row = loadtxt.shape[0]

# 数组的列数
col = loadtxt.shape[1]

print(row)
print(col)
time = loadtxt[0][0]

loadtxt_ = loadtxt[0:, 1:]
loadtxt__ = loadtxt_[1::4]

# 将二维数组转换为一维数组
loadtxt___ = list(map(float, loadtxt__.flatten()))

x = numpy.arange(0, 96, 1)

print(len(loadtxt___))

z1 = numpy.polyfit(x, loadtxt___, 20)
p1 = numpy.poly1d(z1)

print(p1)

y = p1(x)

plot1 = pylab.plot(x, loadtxt___, '*', label='original values')
plot2 = pylab.plot(x, y, 'r', label='fit values')
pylab.title('')
pylab.xlabel('')
pylab.ylabel('')
pylab.legend(loc=3, borderaxespad=0., bbox_to_anchor=(0, 0))
pylab.show()
pylab.savefig('p1.png', dpi=200, bbox_inches='tight')

# integrate.trapz(loadtxt___, x)

print(time)
print(loadtxt___)
