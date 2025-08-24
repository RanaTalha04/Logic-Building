# Find minimums of numbers:

# Without built-in Function:

def min(a, b):
    if a > b:
        return b
    else:
        return a


a = int(input("Enter a number: "))
b = int(input("Enter another numbers: "))
min_num = min(a, b)
print(min_num)


# with Buit-in Function:

def min_numb(a, b):
    return min(a, b)

a = int(input("Enter a number: "))
b = int(input("Enter another numbers: "))
min_num = min_numb(a, b)
print(min_num)