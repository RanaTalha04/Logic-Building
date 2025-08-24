# 🔹 Task 1: Reverse a String (without built-ins)

user_input = input("Enter a string (word) to reverse it: ")
len_user_input = len(user_input)
new_string = ""
print(len_user_input)
for char in range(len_user_input-1,-1, -1):
    new_string += user_input[char]

print(new_string)