def fibonacci_sequence(n):
    sequence = [0, 1]  
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci_seq = fibonacci_sequence(num_terms)
print("Fibonacci sequence:")
for num in fibonacci_seq:
    print(num, end=" ")
