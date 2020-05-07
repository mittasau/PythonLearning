def calculateSum(num):
    if num < 2:
        return 0
    else:
        return num + calculateSum(num-1)
 
res = calculateSum(20)
print(res)