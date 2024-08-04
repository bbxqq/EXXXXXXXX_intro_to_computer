import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# 打开文件并读取内容
with open('Temperature.txt', 'r') as file:
    content = file.readlines()

# 解析每一行并去掉不需要的部分，将每行数据存储到列表中
all_data = []
for line in content:
    # 去掉行首的 'Tainan:'，如果存在
    if line.startswith('Tainan:'):
        continue
    # 去掉每行开头的年份并将每行数据存储到列表中
    data = [float(value) for value in line.strip().split(', ')[1:]]
    all_data.append(data)

# 使用 pprint 模块打印数据
print("All data (as floats):")
print(all_data)
m = np.arange(1, 13)
print(m)
print(type(m))
print(m)
year = 2013
for i in all_data:
    year_s = str(year)
    plt.plot(m, i, label=year_s)
    year += 1


plt.title('tainan temp')
plt.xlabel('Month')
plt.ylabel('Temp')
#plt.xticks(x)
plt.legend()
plt.show()