def function(input:str) -> list[str]:
    if len(input) == 0:
        return []
    if len(input) == 1:
        return input
        
    result = []
    for i in range(len(input)):
        c = input[i] #放在開頭的數字
        r = input[:i] + input[i+1:] #剩餘數字
        
        for j in function(r):
            result.append(c + j)
    return result

print(function('1234'))