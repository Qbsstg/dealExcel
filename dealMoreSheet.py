import numpy
import pandas
from scipy import integrate

filename = 'sheet.xlsx'
# wb = openpyxl.load_workbook(filename)
# sheet = wb.get_sheet_by_name('Sheet1')
# print(sheet.max_row)

fn = open(filename, 'r', encoding='utf-8')

excel = pandas.read_excel(filename, sheet_name=None, header=None)

a_excel = excel['A']

loadtxt = a_excel.to_numpy()

row = loadtxt.shape[0]

col = loadtxt.shape[1]

time = loadtxt[0][0]

loadtxt_ = loadtxt[0:, 1:]
loadtxt__ = loadtxt_[1::4]

# 将二维数组转换为一维数组
loadtxt___ = list(map(float, loadtxt__.flatten()))

print(loadtxt___)

x = numpy.arange(0, 96, 1)

print(len(loadtxt___))

z1 = numpy.polyfit(x, loadtxt___, 20)
p1 = numpy.poly1d(z1)

print(p1)

v, quad = integrate.quad(p1, 17, 19)

print(1950 * 2 - v)
