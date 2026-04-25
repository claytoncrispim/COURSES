# Challenge: Write a custom annotation that handles bad arguments.
# Definition: Create a custom annotation that checks if all arguments passed to a function are integers. If any argument is not an integer, raise a custom exception with an appropriate error message.

# Given code:
# class NonIntArgumentException(Exception):
#     pass

# def handleNonIntArguments(func):
#     def wrapper(*args):
#         func(*args)
#     return wrapper

# Solution:
class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        for item in args:
            if type(item) is not int:
                raise NonIntArgumentException() # Instructor's solution
                # raise NonIntArgumentException(f"Argument '{item}' is not an integer!") #  Copilot generated error message (more informative)
        return func(*args)
    return wrapper

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

# Test cases
print(sum(1, 2, 3)) # 6
# print(sum(1.0, 2.0, 3.0)) # Error: NonIntArgumentException
print(sum(1, 2, '3')) # Error: NonIntArgumentException
# print(sum(None, None, None)) # Error: NonIntArgumentException