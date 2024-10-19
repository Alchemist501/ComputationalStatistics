import numpy as np

def calculate_statistics(array):
    mean = np.mean(array)
    variance = np.var(array)
    std_deviation = np.std(array)
    return mean, variance, std_deviation

def input_array(prompt):
    while True:
        try:
            array_input = input(prompt)
            array = np.array(list(map(float, array_input.split())))
            return array
        except ValueError:
            print("Invalid input. Please enter numeric values separated by spaces.")

array = input_array("Enter an array of numbers (space-separated): ")
mean, variance, std_deviation = calculate_statistics(array)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

