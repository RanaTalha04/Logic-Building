# Factorial of a Number

# Recursive method
def factorial(n):
    if n == 0 or n == 1:
        return 1
    # print(f"Explaination: {n}! = {n}")
    if n > 1:
        return n * factorial(n - 1)
    

print(factorial(6))

# While-Loop
n = 6
fac = 1

while n > 0:
    fac = fac * n
    n = n - 1
print(fac)


# For-loop
for i in range(1, n + 1):
    fac = fac * i

print(fac)