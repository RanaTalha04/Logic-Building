# Linear & binary search

def linear_Search(arr, tar):
    for i in range(len(arr) - 1):
        if arr[i] == tar:
            return i
    return "Not found"

numbers = input("Enter the array like this (1 2 3): ").split()
target = int(input("Enter the target value you want to find: "))
array = [int(x) for x in numbers]
search = linear_Search(array, target)
print(f"Value found at index: {search}")