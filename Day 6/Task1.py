# Check if it is a Prime Number
import math

def is_prime(num):
    if num <= 1:
        return "Not Prime"
    if num == 2:
        return "Prime"
    if num % 2 == 0:
        return "Not Prime"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return "Not Prime"
    return "Prime"


num = int(input("Enter a number to check if it is a prime number: "))
prime = is_prime(num)
print(prime)
