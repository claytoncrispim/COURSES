# Question 1 of 3:
# What will be printed when this code is run?
var1 = 1
var2 = 2
def someFuncA(var1):
    print(f'{var1}, {var2}')

someFuncA(3)
# 1st option: 2, 1
# 2nd option: 2, 3
# 3rd option: 1, 2
# 4th option: 3, 2 (correct answer)


# Question 2 of 3:
# What is not a valid way to call a function with this definition?

# def someFunc(var1, var2, var3, var4):

# 1st option: someFunc(var1=1, var2=2, var4=4, var3=3)
# 2nd option: someFunc(1,2,3,4)
# 3rd option: someFunc(1, 2, var4=4, var3=3)
# 4th option: someFunc(var1=1,2,3,4) (correct answer)


# Question 3 of 3:
# What will be printed when this code is run?
def someFuncB(func):
    print(func(5) + 2)

someFuncB(lambda x: x * 3)

# 1st option: 17 (correct answer)
# 2nd option: 21
# 3rd option: 7
# 4th option: 11