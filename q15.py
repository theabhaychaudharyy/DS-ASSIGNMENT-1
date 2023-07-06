def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_lst[n // 2]
    return median
input_list = input("Enter a list of numbers, separated by spaces: ").split()
input_list = [float(num) for num in input_list]  # Convert input to a list of floats
median = find_median(input_list)
print("Median of the list:", median)
