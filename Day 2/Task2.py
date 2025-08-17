# 🔹 Task 2: Reverse a Number (without string conversion)

num = int(input("Enter a number to reverse: "))
rev_num = 0

while num > 0:
    rm = num % 10
    rev_num = rev_num * 10 + rm
    num = num // 10

print(rev_num)