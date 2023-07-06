def remove_duplicates(lst):
    return list(set(lst))
input_list = input("Enter a list of elements, separated by spaces: ").split()
unique_elements = remove_duplicates(input_list)
print("List with duplicate elements removed:", unique_elements)
