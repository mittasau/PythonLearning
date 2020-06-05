def inrementor(m):
    # inner function operation
    def operation(n):
        # n is incremented by m
        return n + m
    # return the inner function
    return operation
 
incrementby1 = inrementor(1)
incrementby5 = inrementor(5)
incrementby9 = inrementor(9)
 
# should print 2
print(incrementby1(1)) 
# should print 6
print(incrementby5(1))
# should print 10
print(incrementby9(1))