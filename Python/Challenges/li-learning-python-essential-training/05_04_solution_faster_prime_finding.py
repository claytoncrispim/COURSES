# Solution by the instructor
def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        sqrtNum = number ** 0.5
        for factor in primes:
            if number % factor == 0:
                # Not a prime number
                break
            if factor > sqrtNum:
                # No need to check any more factors
                primes.append(number)
                break
    return primes

print(allPrimesUpTo(1000))