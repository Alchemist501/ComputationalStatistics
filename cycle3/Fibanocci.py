import numpy as np

def fibonacci_binet(n):
    # Define the golden ratio and sqrt(5)
    phi = (1 + np.sqrt(5)) / 2
    sqrt5 = np.sqrt(5)
    
    # Calculate the nth Fibonacci number using Binet's formula
    fib_n = (phi**n - (1 - phi)**n) / sqrt5
    
    # Round the result to get the nearest integer
    return round(fib_n)

# Generate Fibonacci sequence up to the 10th term as an example
n_terms = 10
fibonacci_series = [fibonacci_binet(n) for n in range(n_terms)]

print("Fibonacci Series using Binet's Formula:")
print(fibonacci_series)
