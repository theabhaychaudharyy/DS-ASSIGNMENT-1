def find_intersection(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection
input_list1 = input("Enter elements for the first list, separated by spaces: ").split()
input_list2 = input("Enter elements for the second list, separated by spaces: ").split()
intersection = find_intersection(input_list1, input_list2)
if not intersection:
    print("There are no common elements between the two lists.")
else:
    print("Intersection of the two lists:", intersection)
