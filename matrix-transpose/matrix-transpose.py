import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    x=np.asarray(A,dtype=float)
    return x.T
