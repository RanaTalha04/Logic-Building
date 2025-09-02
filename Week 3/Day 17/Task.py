# Selection sort 

def Selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
          if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] 
    return arr 

numbers = input("Enter the array (space-separated): ").split()
array = [int(x) for x in numbers]
selection = Selection_sort(array)
print(f"Sorted array is: {selection}")

# Quick sort 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

numbers = input("Enter the array (space-separated): ").split()
array = [int(x) for x in numbers]
quick = quick_sort(array)
print(f"Sorted array is: {quick}")