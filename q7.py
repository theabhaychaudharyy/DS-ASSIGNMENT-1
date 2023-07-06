def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
input_number = int(input("Enter a number: "))
factorial_result = factorial(input_number)
if factorial_result is None:
    print("Factorial is undefined for negative numbers.")
else:
    print("Factorial of", input_number, "is:", factorial_result)
