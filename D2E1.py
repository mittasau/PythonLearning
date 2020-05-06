list1 = ["A", "B", "C", "D"] 
list2 = ["E", "F", "G", "H"]

list3 = [i + j for i, j in zip(list1, list2)]

print(list3)