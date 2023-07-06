def sort_list(lst):
    sorted_list = sorted(lst)
    return sorted_list
input_list = input("Enter a list of integers, separated by spaces: ").split()
input_list = [int(num) for num in input_list]  
sorted_list = sort_list(input_list)
print("Sorted list in ascending order:", sorted_list)
