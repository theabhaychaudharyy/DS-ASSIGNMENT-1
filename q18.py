def max_subarray_sum(lst):
    if not lst:
        return None
    max_sum = lst[0]
    current_sum = lst[0]
  for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
input_list = input("Enter a list of numbers, separated by spaces: ").split()
input_list = [int(num) for num in input_list]  
max_sum = max_subarray_sum(input_list)
if max_sum is None:
    print("The list is empty.")
else:
    print("Maximum subarray sum:", max_sum)
