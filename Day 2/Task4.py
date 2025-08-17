# 🔹 Task 4: Palindrome Number

def Palindrome_Num(num):
    original_num = num
    rev_num = 0

    while num > 0:
        rm = num % 10
        rev_num = rev_num * 10 + rm
        num = num // 10

    if rev_num == original_num:
        return "Palindrome"
    else:
        return "Not Palindrome"

num = int(input("Enter a number to reverse: "))
is_Palindrome = Palindrome_Num(num)

print(is_Palindrome)