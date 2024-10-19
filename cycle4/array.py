import numpy as np

def input_array(prompt):
    while True:
        try:
            array_input = input(prompt)
            array = np.array(list(map(float, array_input.split())))
            return array
        except ValueError:
            print("Invalid input. Please enter numeric values separated by spaces.")

array = input_array("Enter the array data (space-separated values): ")
array_reshaped = array.reshape(-1, 1)  
filename = "output.csv"
np.savetxt(filename, array_reshaped, delimiter=",", header="Values", comments='', fmt='%s')
print("Array has been saved to "+str(filename)+".")

