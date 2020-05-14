# PythonLearning
D1E1 Print the following: -  “Hello ATS Team” 

D1E2 Create a string, integer and float. Print String only if it is “hello”, print integer if it is 2020 and print float if it is 1.0 

D1E3 Input two numbers and perform addition, multiplication 

D2E1  Concatenate two lists on each index 
    list1 = ["A", "B", "C", "D"]  
    list2 = ["E", "F", "G", "H"] 

    Expected op:  >> ['AE', 'BF', 'CG', 'DH'] 

D2E2  Print 

        1  

        1 2  

        1 2 3  

        1 2 3 4  

        1 2 3 4 5 

D2E3  For an input string count all upper case, lower case, numbers, and special characters 

D3E1  Write a recursive function calculating the sum of numbers from 2 to 20 

D3E2   Given a list iterate it and display numbers which are divisible by 3 and if you find number greater     than 150 stop the loop iteration 

list1 = [12, 14, 33, 43, 55, 75, 99, 132, 150, 180, 200] 

D3E3  Describe the scope of the variables a, b, c and d in this example: 

        def my_function(a):     

        b = a - 2 

        return b 

            c = 3 

        

            if c > 2:     

        d = my_function(5) 

        print(d) 

        What is the lifetime of these variables? When will they be created and destroyed? 

        Can you guess what would happen if we were to assign c a value of 1 instead? 

        Why would this be a problem? Can you think of a way to avoid it? 

D4E1   Write a class for cars. Create two new cars called carA and carB. Set carA to be a black sedan worth $50000 with a name of Ford, and car2 to be        a red truck named Jeep worth $10000 

D4E2 Write a Python class to reverse a string by words 

        Input string : 'hello ATS' 
        Expected Output : 'ATS hello' 

D4E3
    Create a set a which contains the first four positive integers and a set b which contains the first four odd positive integers. 

    Create a set c which combines all the numbers which are in a or b (or both). 

    Create a set d which contains all the numbers in a but not in b. 

    Create a set e which contains all the numbers in b but not in a. 

    Create a set f which contains all the numbers which are both in a and in b. 

    Create a set g which contains all the numbers which are either in a or in b but not in both. 

    Print the number of elements in c. 

 
D4E4  Create a dict directory which stores telephone numbers (as string values), and populate it with these key-value pairs: 

        Name 

        Telephone number 

        Jane Doe 

        +27 555 5367 

        John Smith 

        +27 555 6254 

        Bob Stone 

        +27 555 5689 

        Change Jane’s number to +27 555 1024 

        Add a new entry for a person called Anna Cooper with the phone number +27 555 3237 

        Print Bob’s number. 

        Print Bob’s number in such a way that None would be printed if Bob’s name were not in the dictionary. 

        Print all the keys. The format is unimportant, as long as they’re all visible. 

        Print all the values. 

D5E1 Sort a tuple of tuples by 2nd item 

    tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29)) 

    Expected output: 

    (('c', 11), ('a', 23), ('d', 29), ('b', 37)) 

D5E2 
    Create a tuple a which contains the first four positive integers and a tuple b which contains the next four positive integers. 

    Create a tuple c which combines all the numbers from a and b in any order. 

    Create a tuple d which is a sorted copy of c. 

    Print the third element of d. 

    Print the last three elements of d without using its length. 

    Print the length of d. 

 
D5E3  Print an alphabetically sorted list of all functions in the numpy module, which contain the word find. 

D6E1: 

    Remove duplicate from a list and print list and create a tuple and find the minimum and maximum number 

    For Example: 

    sampleList = [1, 4, 1, 5, 4, 4, 9, 9] 


D6E2: 

    Implement Bubble Sort 

    Compare first and second element in the list and swap if they are in the wrong order. 

    Compare second and third element and swap them if they are in the wrong order. 

    Proceed similarly until the last element of the list in a similar fashion. 

    Keep repeating all of the above steps until the list is sorted. 


D6E3: 

    Write a Python program to create a FIFO queue and a LIFO queue. 


D7E1:   Exception Handling 

        Type something so that Python gives a NameError. 

        Type something so that Python gives a SyntaxError.  

        Type something so that Python gives a TypeError. 

        Type something so that Python gives a IndexError. 

        Type something so that Python gives a KeyError. 

        Type something so that Python gives a AttributeError. 

        Type something so that Python gives a ValueError. 

D7E2: 

    Write an interactive calculator. 

    User input should be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1)

    Split user input using str.split(), and check whether the resulting list is valid: 

    If the input does not consist of 3 elements, raise a ExpressionError, which is a custom Exception. 

    Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a ExpressionError 

    If the second input is not '+' or '-', again raise a ExpressionError 

    On valid input, perform the calculation and print out the result. Do this, until the user enters quit. 

    An interaction could look like this: 

    > 2 + 2 
    4.0 
    >>> 4.6 - 1.2 
    3.3999999999999995 
    >>> quit 
    >>> 1 + 12.0
    >>> 3.2 - 1.51.7000000000000002>
    >> quit 

 

D8E1:  

    Open a CSV file which contains three columns of numbers. Write out the data to a new CSV file, swapping around the second and third columns and adding a fourth column which contains the sum of the first three. 

D8E2: 

    Write a Python program to convert Python objects into JSON strings. Print all the values. 

    Dict, list, string, integer, float, boolean, null 

D8E3:

    Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content. 

D9E1:
    Write Python code to create a SQLite database. Make a connection with the database and print the version of the SQLite database. 

D9E2:

    Write Python code to create a table and insert some records. Then selects all rows from the same table and display the records. 

D9E3 : 

    Write a Python code to insert values to a table from user input. 

 
 