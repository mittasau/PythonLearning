1. Describe the scope of the variables a, b, c and d in this example: 

def my_function(a):     

    b = a - 2 

    return b 

c = 3 

 

if c > 2:     

    d = my_function(5) 

    print(d) 

2. What is the lifetime of these variables? When will they be created and destroyed? 

3. Can you guess what would happen if we were to assign c a value of 1 instead? 

4. Why would this be a problem? Can you think of a way to avoid it? 

## a, b is local variable. c, d is global scope

## a,b gets created and destroyed within function. c and d gets created when assigned and remains till end of execution

## d will not get created

## assign d some default value at the start
