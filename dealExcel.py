import pandas

# 读取所有的sheet
filename = 'train2.xlsx'
excel = pandas.read_excel(filename, sheet_name=None, header=None)

# 取出A的数据
a_to_numpy = excel['A'].to_numpy()

# 定义一个常量
c = 0
