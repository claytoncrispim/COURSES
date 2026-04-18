from datetime import datetime

# Question 1 of 4:
wait_until = datetime.now().second + 2    
while datetime.now().second != wait_until:
    print('Still waiting!')

print(f'We are at {wait_until} seconds!')



# ------------------------------------------------------------

# Question 2 of 4:
# What list does this statement generate?
['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)]


# ['Monty Python', 2, 'Python', 'Monty', 5, 'Monty Python', 7, 'Monty', 'Python']

# ['Monty Python', 'Monty', 'Python', 'Monty', 5, 'Monty Python', 7, 'Monty', 'Python']

# [1, 'Python', 'Monty', 'Python', 5, 'Monty Python', 7, 'Python', 'Monty']

# [1, 'Monty', 'Python', 'Monty', 5, 'Monty Python', 7, 'Monty', 'Python'] # Correct


# Explanation: The list comprehension iterates through the numbers 1 to 9 and applies a series of conditional checks to determine what to include in the resulting list.
# It checks if the number is divisible by 6 first, then 3, then 2. If it is divisible by 6, it returns 'Monty Python'. If it is divisible by 3 but not 6, it returns 'Python'. If it is divisible by 2 but not 6, it returns 'Monty'. If it is not divisible by either 2 or 3, it returns the number itself.
print(['Monty Python' if n % 6 == 0 else 'Python' if n % 3 == 0 else 'Monty' if n % 2 == 0 else n for n in range(1, 10)])

# ------------------------------------------------------------

# Question 3 of 4:
# Will the print statement be reached in this code?

for number in range(1, 9):
    if number % 10 == 0:
        break
else:
    print('Let\'s print something out!')

# Yes, the print statement will be reached. The for loop iterates through the numbers 1 to 8, and since none of these numbers are divisible by 10, the break statement is never executed. Therefore, the else block associated with the for loop is executed, and the print statement is reached.


# ------------------------------------------------------------

# Question 4 of 4:
# Will the print statement be reached in this code?

for number in range(1, 100):
    if number % 10 == 0:
        break
else:
    print('Let\'s print something out!')

# No, the print statement will not be reached. The for loop iterates through the numbers 1 to 99, and when it reaches the number 10, which is divisible by 10, the break statement is executed. This causes the loop to exit immediately, and the else block associated with the for loop is not executed. Therefore, the print statement is not reached.