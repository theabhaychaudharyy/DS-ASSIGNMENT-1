def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements
input_list1 = input("Enter elements for the first list, separated by spaces: ").split()
input_list2 = input("Enter elements for the second list, separated by spaces: ").split()

common_elements = find_common_elements(input_list1, input_list2)
if not common_elements:
    print("There are no common elements between the two lists.")
else:
    print("Common elements:", common_elements)
