# Question 1 of 3:
# Why is the self variable used inside a class?

# 1st option: 
# It's a Python keyword that refers to the class instance.
# Incorrect: self is not a Python keyword, but it is a convention to use it as the first parameter in instance methods to refer to the instance of the class.

# 2nd option:
# It's a Python keyword used to create static properties on the class.
# Incorrect: self is not a Python-recognized keyword.

# 3rd option:
# It's the conventional variable name to refer to the class instance.
# Correct: self is the conventional variable name used to refer to the instance of the class.


# 4th option:
# It's the conventional variable name used to create static properties on the class.
# Incorrect: self is not used to create static properties; it's used to refer to instance properties.

# Summary:
# self is an instance of the class.

# -------------------------------------------

# Question 2 of 3:
# What is super() used for inside a class?

# 1st option:
# to get an instance of the child class
# Incorrect: super() is used to refer to the parent class, not the child class.

# 2nd option:
# to get the child class name
# Incorrect: super() does not return the child class name; it returns a proxy object that allows you to call methods of the parent class.

# 3rd option:
# to get parent class name
# Incorrect: super() does not return the parent class name; it returns a proxy object that allows you to call methods of the parent class.

# 4th option:
# to get an instance of the parent class
# Correct: super() is used to refer to the parent class and allows you to call its methods.


# -------------------------------------------

# Question 3 of 3:
# Assuming that rover is an instance of the Dog class, what is an equivalent of this line of code?

# rover.speak()

# 1st option:
# rover.speak(Dog)
# Incorrect: rover.speak() is an instance method call, and it does not require the class name as an argument.

# 2nd option:
# Dog.rover.speak()
# Incorrect: This is not valid syntax in Python.

# 3rd option:
# Dog.speak(rover)
# Correct: This is equivalent to rover.speak() because it explicitly passes the instance as the first argument.

# 4th option:
# Dog.speak(self)
# Incorrect: self is not defined in this context; it is only used inside class methods.