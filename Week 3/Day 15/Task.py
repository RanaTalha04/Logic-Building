# Linear search

def linear_Search(arr, tar):
    for i in range(len(arr) - 1):
        if arr[i] == tar:
            return i
    return "Not found"

numbers = input("Enter the array (space-separated): ").split()
target = int(input("Enter the target value you want to find: "))
array = [int(x) for x in numbers]
search = linear_Search(array, target)
print(f"Value found at index: {search}")


# binary search

def binary_search(arr, tar):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            low = mid + 1
        else:
            high = mid - 1
    return "Not found"


numbers = input("Enter the array (space-separated): ").split()
target = int(input("Enter the target value you want to find: "))
array = sorted([int(x) for x in numbers])
print(array)
search = binary_search(array, target)
print(f"Value found at index: {search}")
