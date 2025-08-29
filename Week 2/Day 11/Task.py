def list_com(lst1, lst2):
    i, j = 0, 0
    result = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j]) 
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])

    return result
    

numbers1 = input("Enter list 1 (space-separated): ").split()
numbers2 = input("Enter list 2 (space-separated): ").split()

list1 = sorted( [int(x) for x in numbers1])
list2 = sorted( [int(y) for y in numbers2])

combined_list = list_com(list1, list2)
print(combined_list)