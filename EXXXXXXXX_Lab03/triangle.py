t1 = int(input('請輸入第一個邊長 :'))
t2 = int(input('請輸入第二個邊長 :'))
t3 = int(input('請輸入第三個邊長 :'))
if ((t1+t2 > t3) and (t1+t3 > t2) and (t2+t3 > t1)) == False: #如果不是三角形
    print('這三個邊長不構成一個合法的三角形')
elif t1 == t2 == t3:
    print('這是正三角形')
elif (t1 == t2) or (t1 == t3) or (t2 == t3):
    print('這是等腰三角形')
else :
    print('這是正常三角形')