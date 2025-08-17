# 🔹 Task 3: Palindrome String

def Palindrome(string):

    len_user_input = len(string)
    new_string = ""
    for char in range(len_user_input-1,-1, -1):
        new_string += string[char]
    
    if string == new_string:
        return "Palindrome"
    else:
        return "Not Palindrome"


user_input = input("Enter a string (word) to reverse it: ")
is_palindrome = Palindrome(user_input)
print(is_palindrome)