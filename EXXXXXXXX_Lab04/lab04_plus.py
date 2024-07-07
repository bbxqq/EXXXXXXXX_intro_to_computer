nums = (input('輸入的list為 : ')).split(', ')
val = input('要刪除的數字是 : ')
length = len(nums)
temp = []

for i in range(length):
    if(nums[i] == val):
        pass
    else:
        temp.append(int(nums[i]))
length = len(temp)
print('刪除後!' + '\n' + 'list長度剩下: ' +str(length) + ', list變成: ' + str(temp))