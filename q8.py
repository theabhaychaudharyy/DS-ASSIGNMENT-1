def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
input_number = int(input("Enter a number: "))
if is_prime(input_number):
    print(input_number, "is a prime number.")
else:
    print(input_number, "is not a prime number.")
