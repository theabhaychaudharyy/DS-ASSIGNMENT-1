def find_second_largest(lst):
    if len(lst) < 2:
        return None
    largest = lst[0]
    second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = nu
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest
input_list = input("Enter a list of numbers, separated by spaces: ").split()
input_list = [int(num) for num in input_list]  
second_largest = find_second_largest(input_list)
if second_largest is None:
    print("The list does not have a second largest number.")
else:
    print("The second largest number in the list is:", second_largest)
