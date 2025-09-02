# # Bubble sort 
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
#     return arr


# numbers = input("Enter the array (space-separated): ").split()
# array = [int(x) for x in numbers]
# bubble = bubble_sort(array)
# print(f"Sorted array is: {bubble}")

# Insertion sort

def insertion_sort(arr):
    n = len(arr)
    for i in range(0, n):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
    return arr 


numbers = input("Enter the array (space-separated): ").split()
array = [int(x) for x in numbers]
insertion = insertion_sort(array)
print(f"Sorted array is: {insertion}")
