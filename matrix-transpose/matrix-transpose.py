import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A_T=np.transpose(A)
    return A_T
A=np.array([[1,2,3],[4,5,6]])
matrix_transpose(A)
