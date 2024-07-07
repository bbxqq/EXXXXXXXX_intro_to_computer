a = ['A', 0, 0, 0, 0]
b = ['B', 0, 0, 0, 0]
c = ['C', 0, 0, 0, 0]
arr = [a, b, c]
subject = ['國文', '數學', '英文']
for i in range(3):
    total = 0
    print('輸入' + arr[i][0] + '學生成績')
    for j in range(1, 4):
        arr[i][j] = int(input(subject[j-1] + ':'))
        total += arr[i][j]
    arr[i][4] = total / 3
    
print(a)
print(b)
print(c)