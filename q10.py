def find_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total
input_list = input("Enter a list of numbers, separated by spaces: ").split()
input_list = [int(num) for num in input_list] 
sum_of_numbers = find_sum(input_list)
print("Sum of numbers in the list:", sum_of_numbers)
