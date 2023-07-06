def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
input_list = input("Enter a list of numbers, separated by spaces: ").split()
input_list = [int(num) for num in input_list]  
if is_sorted(input_list):
    print("The list is sorted in non-decreasing order.")
else:
    print("The list is not sorted in non-decreasing order.")
