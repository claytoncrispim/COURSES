def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num - 1) # square is the sum of two triangles, one with num and one with num - 1 => e.g. 7^2 = 7 + 6 + 5 + 4 + 3 + 2 + 1 + 6 + 5 + 4 + 3 + 2 + 1 = 49 (28 + 21)


print(f'triangle(4) = {triangle(4)}') # 4 + 3 + 2 + 1 = 10
print(f'square(4) = {square(4)}') # 4^2 = 4 + 3 + 2 + 1 + 3 + 2 + 1 + 0 = 16 (10 + 6)
print(f'triangle(5) = {triangle(5)}') # 5 + 4 + 3 + 2 + 1 = 15
print(f'square(5) = {square(5)}') # 5^2 = 5 + 4 + 3 + 2 + 1 + 4 + 3 + 2 + 1 = 25 (15 + 10)
print(f'triangle(6) = {triangle(6)}') # 6 + 5 + 4 + 3 + 2 + 1 = 21
print(f'square(6) = {square(6)}') # 6^2 = 6 + 5 + 4 + 3 + 2 + 1 + 5 + 4 + 3 + 2 + 1 = 36 (21 + 15)
print(f'triangle(7) = {triangle(7)}') # 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28
print(f'square(7) = {square(7)}') # 7^2 = 7 + 6 + 5 + 4 + 3 + 2 + 1 + 6 + 5 + 4 + 3 + 2 + 1 = 49 (28 + 21)

# Obs: Instructor's solution was exactly the same as mine.

# Also the instructors says that the triangle function is not very different from the factorial function. We just have to change the operator from multiplication to addition and change the base case from 0 to 1. E.g. factorial(5) = 5 * 4 * 3 * 2 * 1 = 120, while triangle(5) = 5 + 4 + 3 + 2 + 1 = 15.
# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)