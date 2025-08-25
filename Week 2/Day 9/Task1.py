# Remove duplicates from a list

def rem_dup(lst):
    updated_lst = []
    for num in lst:
        if num not in updated_lst:
            updated_lst.append(num)
    return updated_lst

numbers = input("Enter list (1 2 3 4) like this: ").split()
numbers = [int(x) for x in numbers]

duplicates = rem_dup(numbers)
print(f"List after duplicate removal: {duplicates}")
