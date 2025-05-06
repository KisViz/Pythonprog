import numpy as np

def foo(mat1: np.ndarray, mat2: np.ndarray, _: str) -> np.ndarray:
    if mat1.shape != mat2.shape:
        size1 = mat1.size
        size2 = mat2.size

        if size1 == size2:
            mat1 = mat1.reshape(mat2.shape)
        else:
            if size1 > size2:
                flat = mat1.flatten()[:size2]
                mat1 = flat.reshape(mat2.shape)
            else:
                flat = mat2.flatten()[:size1]
                mat2 = flat.reshape(mat1.shape)

    return mat1 * mat2


a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20, 30, 40])
print(foo(a, b, "teszt"))
# Output: [[10 40]
#          [90 160]]
