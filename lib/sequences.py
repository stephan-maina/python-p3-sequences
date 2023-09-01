#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
        print(fibonacci_sequence)

# Example usage:
print_fibonacci(0)  # Prints []
print_fibonacci(1)  # Prints [0]
print_fibonacci(2)  # Prints [0, 1]
print_fibonacci(10) # Prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
