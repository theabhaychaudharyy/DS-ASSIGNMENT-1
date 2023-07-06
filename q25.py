def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list
input_list1 = input("Enter elements for the first sorted list, separated by spaces: ").split()
input_list2 = input("Enter elements for the second sorted list, separated by spaces: ").split()

list1 = [int(num) for num in input_list1]  
list2 = [int(num) for num in input_list2]  

merged_list = merge_sorted_lists(list1, list2)
print("Merged list:", merged_list)
