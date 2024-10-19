import numpy as np

def get_2d_diagonals(array_3d):
    diagonals = []
    if array_3d.ndim != 3:
        raise ValueError("Input must be a 3D array.")
    for i in range(array_3d.shape[0]):
        slice_2d = array_3d[i]
        main_diag = np.diagonal(slice_2d)
        diagonals.append(main_diag)
        anti_diag = np.diagonal(np.fliplr(slice_2d))
        diagonals.append(anti_diag)
    return diagonals

array_3d = np.random.randint(0, 10, (3, 4, 4)) 
result = get_2d_diagonals(array_3d)
for idx, diag in enumerate(result):
    print("Diagonal " + str(idx+1)+": "+ str(diag))

