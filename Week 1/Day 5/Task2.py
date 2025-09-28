# Perfect Number

def Perfect_numb(number):
    total = 0
    for i in range(1,number-1):
        if number % i == 0:
            total = total + i
    if total == number:
        return "Perfect"
    else:
        return "Not Perfect"


num_input = int(input("Enter a number: "))
print(Perfect_numb(num_input))