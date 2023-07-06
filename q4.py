def count_occurrences(lst):
    occurrences = {}

    for element in lst:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 
    return occurrences
input_list = input("Enter a list of elements, separated by spaces: ").split()
occurrences = count_occurrences(input_list)
print("Element occurrences:")
for element, count in occurrences.items():
    print(element, "-", count)
