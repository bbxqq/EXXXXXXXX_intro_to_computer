#定義dict0
dict0 = {'index':['國文', '英文', '數學', '自然', '社會'], 'StuA':[50, 60, 70, 80, 90], 'StuB':[57, 86, 73, 82, 43], 'StuC':[97, 96, 86, 97, 83]}
print(dict0)
print('')

#計算個學生平均成績
def averageStu(values):
    total = 0
    for i in range(len(values)):
        total += values[i]
    return total/len(values)
print('A學生平均成績 : ' + str(averageStu(dict0['StuA'])))
print('B學生平均成績 : ' + str(averageStu(dict0['StuB'])))
print('C學生平均成績 : ' + str(averageStu(dict0['StuC'])))
print('')

#計算各科目平均成績
index = list(dict0['index'])
stuA = list(dict0['StuA'])
stuB = list(dict0['StuB'])
stuC = list(dict0['StuC'])
averageSub = []
for i in range(len(index)):
    temp = (stuA[i] + stuB[i] + stuC[i])/3
    averageSub.append(temp)
    print(index[i] + '平均成績 : ' + str(averageSub[i]))

