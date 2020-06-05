#defining nested function
def outer(message):
    #text is having the scope of outer function
    text = message
    def inner():
        #using non-local variable text
        print(text)
    #return inner function
    return inner 

# main method
if __name__=='__main__':
    func = outer('Hello!')
    func()