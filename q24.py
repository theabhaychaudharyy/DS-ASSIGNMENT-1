def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
input_number = int(input("Enter a number: "))
if is_power_of_two(input_number):
    print(input_number, "is a power of two.")
else:
    print(input_number, "is not a power of two.")
