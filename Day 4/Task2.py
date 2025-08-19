# Fibonacci Sequence

# Recursive method
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)
n = 7    
for i in range(n):
    print(fib(i), end=" ")

# For-loop
print()

prev = 0
next = 1

print(prev, end=" ")
print(next, end=" ")

for i in range(2, n):
    curr = next + prev
    print(curr, end=" ")
    prev = next
    next = curr
