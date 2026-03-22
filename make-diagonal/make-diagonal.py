import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v=np.array(v, dtype=float)
    A=np.zeros((len(v), len(v)))
    for i in range(len(v)):
        A[i,i]=v[i]
    return A
    pass
