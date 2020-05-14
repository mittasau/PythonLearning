#You’ll get a NameError when an object can’t be found in Python.
print(zzz)

#You’ll get a SyntaxError when you make a syntax error in Python. It can be a missing quote or parenthesis.
print("Hello World!"

#You’ll get a TypeError when you apply an operation or function to the wrong type of data, such as applying arithmetic operations to strings.
str = "Hello"
str = str + 5

#You’ll get an IndexError when you try to reach an index outside the limits of your data.
str = "Hello"
print(str[10])

#KeyError is like IndexError for dictionaries. If you try to reach a key that’s not included in your dictionary, you’ll get a KeyError
dict = {1:111, 2:222, 3:333}
print(dict[5])

#AttributeError will occur when you try to apply a method or attribute to the wrong data type which doesn’t have that method.
str = "Hello"
str.reverse()

""" Value error occurs when you apply a function to a data type correctly but the content is not suitable for that operation. For example, you can apply int() to a string of numbers such as:
int(“111”)
but you can’t convert letters to integers so following won’t work:
int(“Hello”) """

str = "moose"
ans_1 = int(str)