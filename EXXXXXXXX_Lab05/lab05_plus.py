dict0 = {}

for i in range(4):
    dict0.setdefault(input('Enter Keys : '), (input('Enter values : ').split(',')))
    
print(dict0)