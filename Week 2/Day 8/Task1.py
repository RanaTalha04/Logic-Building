# Find maximum of numbers:
# Without built-in Function:

def max(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Enter a number: "))
b = int(input("Enter another numbers: "))
max_num = max(a, b)
print(max_num)


# with Buit-in Function:


def max_numb(a, b):
    return max(a, b)

a = int(input("Enter a number: "))
b = int(input("Enter another numbers: "))
max_num = max_numb(a, b)
print(max_num)