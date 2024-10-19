import numpy as np

def get_2d_array_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Please enter the elements of the array row by row (space-separated):")
    array_data = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: You must enter exactly "+str(cols)+" numbers for each row.")
            return None
        array_data.append(row)
    array_2d = np.array(array_data)
    return array_2d
    
array_2d = get_2d_array_from_user()

if array_2d is not None:
    print("You entered the following 2D array:")
    print(array_2d)
    flattened_array = array_2d.flatten()
    print("Flattened array:", flattened_array)

