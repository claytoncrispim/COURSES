# def factorial(num):
#     if num < 0 and type(num) != int:
#         return None
    
#     current = 0
#     next = 0
#     result = 1
#     new_result = 1
#     i = num
#     while num >= 1:
#         print("Loop starts:")    
#         print("num =", num)

#         current = num
#         print("current =", current)

#         result = current * (current -1)
#         new_result = result
#         print("result =", result)

#         num = current - 1
#         next = num
#         print("next =", next)
        
#         final = new_result * next
#         print("final", final)


#         print("------- Loop ends -------")

#     return num

 


# factorial(5)
# # print(factorial(5))

# n = 5
# i = 0
# # while a >= 1:
# #     print(a)
# #     a = a - 1


# # while a >= 1:
# #     print("a =", a)
# #     print(a * (a -1))
# #     a = a - 1

# next = 0
# current = 0
# while n >= 1:
#     print("Loop starts:")    
#     print("n =", n)

#     current = n
#     print("current =", current)

#     result = current * (current -1)
#     print("result =", result)

#     n = current - 1
#     next = n
#     print("next =", next)

#     print("------- Loop ends -------")


# def factorial(num):
#     if num < 0 and type(num) != int:
#         return None
    
#     results = []
#     next = 0
#     current = 0

#     while num >= 1:
#         print("num =", num)
#         print("num * (num -1)=", num * (num -1))
#         results.append(num * (num -1))
#         print("RESULTS:", results)
#         num = num - 1
#     # while num >= 1:
#     #     print("----- Loop starts: -----")    
#     #     print("num =", num)

#     #     current = num
#     #     print("current =", current)

#     #     result = current * (current -1)
#     #     print("result =", result)

#     #     num = current - 1
#     #     next = num
#     #     print("next =", next)

#     #     r = result * next
#     #     results.append(r)
#     #     print("RESULTS LIST:", results)

#     #     print("------- Loop ends -------")


# def factorial(num):
#     if num < 0 and type(num) != int:
#         return None
    
#     i = 0
#     s = 0

#     while i < num:
#         print("   ")
#         print("   ")

#         print("---- LOOP BEGINS ---- ")
#         print("   ")
#         print("BEFORE SUM i =", i, ", and s =", s)
#         print("   ")

#         i = i + 1
#         print("i = i + 1 = ", i)
#         print("Now i =", i, "and s =", s)
#         print("   ")

#         s = s + i
#         print("s = s + i = ", s)
#         print("Now i =", i, "and s =", s)

#         print("   ")

#         print("---- LOOP ENDS ----")

#     return "return", s






# def factorial(num):
#     if num < 0 and type(num) != int:
#         return None
    
#     i = num
#     s = 0

#     while i < 0:
#         print("   ")
#         print("   ")

#         print("---- LOOP BEGINS ---- ")
#         print("   ")
#         print("BEFORE operation i =", i, ", and s =", s)
#         print("   ")

#         i = i + 1
#         print("i = i - 1 = ", i)
#         print("Now i =", i, "and s =", s)
#         print("   ")

#         s = s + i
#         print("s = s + i = ", s)
#         print("Now i =", i, "and s =", s)

#         print("   ")

#         print("---- LOOP ENDS ----")

#     return "return", s




# # Almost there ********
# def factorial(num):
#     if num < 0 and type(num) != int:
#         return None
   
#     i = num
#     s = 1
#     r = 0
#     f = 0
#     while i > 0:
#         print("   ")
#         print("   ")
#         print("---- LOOP BEGINS ---- ")
#         print("   ")
#         print("BEFORE operation i =", i, ", s =", s, ", r =", r, "and f =", f)
#         print("   ")
#         i = i -1
#         s = num * i
#         r = s * (i - 1)
#         f = r * ((i - 1)-1)
#         print("AFTER operation i =", i, ", s =", s, ", r =", r, "and f =", f)
#         print("   ")
#         print("---- LOOP ENDS ----")
  
#     return f
        


# def factorial(num):
    
   
#     i = num
#     s = 1
#     r = 0
#     f = 0
  
#     if num < 0 and type(num) != int:
#         return None
#     else:
#         print("   ")
#         print("   ")
#         print("---- LOOP BEGINS ---- ")
#         print("   ")
#         print("BEFORE operation i =", i, ", s =", s, ", r =", r, "and f =", f)
#         print("   ")
#         i = i -1
#         s = num * i
#         r = s * (i - 1)
#         f = r * ((i - 1)-1)
#         print("AFTER operation i =", i, ", s =", s, ", r =", r, "and f =", f)
#         print("   ")
#         print("---- LOOP ENDS ----")
  
#     return f
        


# SOLUTIONS By the Instructor
def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None

    factorial = 1 # the factorial we'll return at the end
    counter = 1 # the variable that will keep track of how many loops we need to do
    while counter <= num:
        factorial = factorial * counter
        counter = counter + 1

    return factorial



print(factorial(0))


# Recursion Solution
# Explanation: A function that calls itself is called a recursive function. In this case, the factorial function calls itself with a smaller value of num until it reaches the base case (when num is 0). The base case returns 1, and the recursive calls build up the factorial value as they return back up the call stack.
# Example: factorial(5) => 5 * factorial(4) => 5 * (4 * factorial(3)) => 5 * (4 * (3 * factorial(2))) => 5 * (4 * (3 * (2 * factorial(1)))) => 5 * (4 * (3 * (2 * (1 * factorial(0))))) => 5 * (4 * (3 * (2 * (1 * 1)))) => 120
def recFactorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None

    if num == 0:
        return 1
    else:
        return num * recFactorial(num - 1)
    

print(recFactorial(6))