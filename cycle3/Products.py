import numpy as np

def inner_product(a, b):
    """Calculate the inner product of two vectors."""
    if len(a) != len(b):
        raise ValueError("Both vectors must be of the same length.")
    return np.sum(a * b)

def outer_product(a, b):
    """Calculate the outer product of two vectors."""
    return np.outer(a, b)

def cross_product(a, b):
    """Calculate the cross product of two 3D vectors."""
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Both vectors must be of length 3.")
    return np.cross(a, b)

# Example usage
vec_a = np.array([1, 2, 3])
vec_b = np.array([4, 5, 6])

# Inner product
inner = inner_product(vec_a, vec_b)
print("Inner Product:", inner)

# Outer product
outer = outer_product(vec_a, vec_b)
print("Outer Product:\n", outer)

# Cross product
cross = cross_product(vec_a, vec_b)
print("Cross Product:", cross)
