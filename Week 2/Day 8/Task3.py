# Find sum of numbers:
# Without built-in Function:

def sum(a, b):
    return a + b


a = int(input("Enter a number: "))
b = int(input("Enter another numbers: "))
sum_num = sum(a, b)
print(sum_num)


# with Buit-in Function:


def sum_numb(a, b):
    return sum(a, b)

a = int(input("Enter a number: "))
b = int(input("Enter another numbers: "))
sum_num = sum_numb(a, b)
print(sum_num)