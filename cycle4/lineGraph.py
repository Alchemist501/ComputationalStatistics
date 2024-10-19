import numpy as np
import matplotlib.pyplot as plt

def input_array(prompt):
    while True:
        try:
            array_input = input(prompt)
            array = np.array(list(map(float, array_input.split())))
            return array
        except ValueError:
            print("Invalid input. Please enter numeric values separated by spaces.")

data = input_array("Enter the y-values of the line graph (space-separated): ")
x_values = np.arange(len(data))
plt.plot(x_values, data, marker='o')  # Optional: add marker to each point
plt.xlabel("Index")
plt.ylabel("Y-values")
plt.title("Line Graph from NumPy Array")
plt.grid()  
plt.show()

