# Task 1: Check if a number is Prime or not.
import math

def Check_prime(num):
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


for i in range(3, 12):
    print(i, Check_prime(i))