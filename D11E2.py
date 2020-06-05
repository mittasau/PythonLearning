def log(original_function, logfilename="log.txt"):
    def new_function(*args, **kwargs):
        print("Before call")
        result = original_function(*args, **kwargs)
        print("After call")
        with open(logfilename, "a") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s. The result was %s.\n" % (original_function.__name__, args, kwargs, result))

        return result

    return new_function


@log
def add(x, y):
    return x + y

@log
def substract(x, y):
    return x + y
   

print(add(3.5, 7))

print(substract(3.5, 1.5))

with open("log.txt", "r") as logfile:
    print(logfile.read())