def find_largest_element(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
input_list = input("Enter a list of numbers, separated by spaces: ").split()
input_list = [int(num) for num in input_list] 
largest_element = find_largest_element(input_list)
if largest_element is None:
    print("The list is empty.")
else:
    print("The largest element in the list is:", largest_element)
