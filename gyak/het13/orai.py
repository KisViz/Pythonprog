import numpy as np

def foo(matrix1, matrix2, mode):
    m1 = np.array(matrix1)
    m2 = np.array(matrix2)

    if m1.shape != m2.shape:
        size1 = m1.size
        size2 = m2.size

        if size1 == size2:
            m1 = m1.reshape(m2.shape)
        else:
            if size1 > size2:
                m1 = m1.flatten()[:size2].reshape(m2.shape)
            else:
                m2 = m2.flatten()[:size1].reshape(m1.shape)

    return m1 * m2
