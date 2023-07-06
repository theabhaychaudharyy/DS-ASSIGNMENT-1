def find_prime_factors(num):
    factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors
input_number = int(input("Enter a number: "))

prime_factors = find_prime_factors(input_number)
if prime_factors:
    print("Prime factors of", input_number, "are:", prime_factors)
else:
    print("The number does not have any prime factors.")
