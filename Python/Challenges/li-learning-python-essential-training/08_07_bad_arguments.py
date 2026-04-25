class NonIntArgumentException(Exception):
    errorType = TypeError
    message = "Not an integer!"
    def __init__(self):
        super().__init__(f'\n Error: {self.errorType} \n Message: {self.message}')

def handleNonIntArguments(func):
    def raiseIntError():
        raise NonIntArgumentException()
    
    def wrapper(*args):
        for arg in args:
            if type(arg) is not int:
                raiseIntError()
            
        return func(*args)

    return wrapper


@handleNonIntArguments
def add(*args):
    return sum(args) 

# Test cases
print(add(1, 2, 3)) # 6
# print(add(1.0, 2.0, 3.0)) # Error: TypeError, Message: Not an integer!
print(add(1, 2, '3')) # Error: TypeError, Message: Not an integer!
# print(add(None, None, None)) # Error: TypeError, Message: Not an integer!