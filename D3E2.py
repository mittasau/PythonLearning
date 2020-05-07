list1 = [12, 14, 33, 43, 55, 75, 99, 132, 150, 180, 200] 
for item in list1:
    if (item > 150):
        break
    if(item % 3 == 0):
        print(item)