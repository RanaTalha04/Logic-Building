# Check if it is a Prime Number
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def Prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    print(primes)
    return sum(primes)

num = int(input("Enter a number to calculate the sum of n prime numbers: "))
prime = Prime(num)
print(prime)
