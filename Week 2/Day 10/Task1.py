# Frequency counter using dict.

def Freq_count(input):
    dictionary = {}
    for char in input:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    return dictionary

string = input("Enter text: ")
output = Freq_count(string)
print(output)