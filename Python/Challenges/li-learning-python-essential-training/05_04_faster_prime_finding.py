def allPrimesUpTo(num):
    primesFound = []        
    
    # 1. Find the square root of the number
    sqrt = int(num ** 0.5)
    print(f'# 1. Find the square root of the number:\n√({num}) =', sqrt)

    # 2. Find all the primes up to that square root
    for number in range(2, num):
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                break        
        else:
                primesFound.append(number)
                # break    

    return primesFound

print(allPrimesUpTo(1000))