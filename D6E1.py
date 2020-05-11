sampleList = [1, 4, 1, 5, 4, 4, 9, 9] 

print("Original list", sampleList)

sampleList = list(set(sampleList))
print("unique list", sampleList)

tuple = tuple(sampleList)
print("tuple ", tuple)

print("Minimum number is: ", min(tuple))
print("Maximum number is: ", max(tuple))