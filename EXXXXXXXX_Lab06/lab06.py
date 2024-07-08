def gcd(a, b, aa=None, bb=None):
    if(aa is None and bb is None):
        aa = a
        bb = b
    if(a == 0 or b == 0):
        print('0 沒有gcd')
        return 0
    rem = a % b
    if(b == 1): 
        print(aa, '和', bb, '互質')
        return 0
    elif(rem == 0):
        print(aa, '和', bb, '的gcd= ', b)
        return 0
    gcd(b, rem, aa, bb)

ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19, 20)