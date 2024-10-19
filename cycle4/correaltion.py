import numpy as np

def input_array(prompt):
    while True:
        try:
            array_input = input(prompt)
            array = np.array(list(map(float, array_input.split())))
            return array
        except ValueError:
            print("Invalid input. Please enter numeric values separated by spaces.")

def pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Arrays must be of the same length.")
    
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    numerator = np.sum((x - mean_x) * (y - mean_y))
    std_x = np.sqrt(np.sum((x - mean_x) ** 2))
    std_y = np.sqrt(np.sum((y - mean_y) ** 2))
    
    if std_x == 0 or std_y == 0:
        return 0  
    
    r = numerator / (std_x * std_y)
    return r


x = input_array("Enter the first array of numbers (space-separated): ")
y = input_array("Enter the second array of numbers (space-separated): ")

try:
    correlation_coefficient = pearson_correlation(x, y)
    print("Pearson correlation coefficient:", correlation_coefficient)
except ValueError as e:
    print(e)

