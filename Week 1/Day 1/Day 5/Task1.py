# Armstrong Number

def Armstrong_numb(number):
    original = int(number)
    length = len(number)
    number = int(number)
    total = 0

    while number > 0:
        remain = number % 10
        number = number // 10
        total = total + (remain ** length)
        
    if total == original:
        return "Armstrong"
    else:
        return "Not Armstrong"


num_input = input("Enter a number: ")
print(Armstrong_numb(num_input))