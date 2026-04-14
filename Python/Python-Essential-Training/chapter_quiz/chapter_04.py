# Question 3 of 5
# You are given these data structure values:

values = [[1, 'i', 'a'], ['2', 'we', 'be', 'it'], [3, 'are', 'few', 'too']]


# Then, you are asked to produce this structure:
structure = {
        1: ['i', 'a'],
        2: ['we', 'be', 'it'],
        3: ['are', 'few', 'too']
}


# Which line of Python will do this?


# # 1
# {key: values for key in values}

# # 2
# {item[0]: item[1:3] for item in values}

# # 3
# {key: value for key, value in values}

# 4 (correct)
myList = {item[0]: item[1:] for item in values}

print('#4 (Correct):', myList)

# --------------------------------------------------

# Question 4 of 5
# How would you write a nested list comprehension to apply a function someFunc to all comments in a list of blog objects?

#1
# [for blog in blogs [someFunc(comment) for comment in blog.comments]]

#2 (correct)
# [[someFunc(comment) for comment in blog.comments] for blog in blogs]

#3
# [[blog for blog in blogs] for someFunc(comment) in blog.comments]

#4
# [for someFunc(comment) in comments [blog.comments for blog in blogs ]]

print('#2 (Correct):', '[[someFunc(comment) for comment in blog.comments] for blog in blogs]')


# ------------------------------------------
# Question 5 of 5
# Which option lists the numbers 100 to 0, backwards, by increments of 5? ([100, 95, 90,..., 0])

print('#1:', list(range(101))[::5])
print('#2:', list(range(101))[:5:-1])
print('#3 (Correct):', list(range(101))[::-5])
print('#4:', list(range(101))[-5::])