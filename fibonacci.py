#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_number_of_terms():
    while True:
        try:
            num = int(input("Enter how many terms you want in the Fibonacci sequence: "))
            if num > 0:
                return num
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_sequence(sequence):
    print("Fibonacci sequence:")
    print(", ".join(map(str, sequence)))

def main():
    n = get_number_of_terms()
    fib_seq = generate_fibonacci(n)
    print_sequence(fib_seq)

if __name__ == "__main__":
    main()
