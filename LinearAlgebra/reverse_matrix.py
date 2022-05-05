import numpy as np


def reverse_matrix(mat): 
    # array = np.zeros(mat.shape[0]*mat.shape[1])
    mat_out = np.zeros_like(mat)
    rows = mat.shape[0]
    cols = mat.shape[1]
    for row in range(rows): 
        for col in range(cols): 
            mat_out[rows-row-1,cols-col-1] = mat[row,col]
    return mat_out

if __name__ == '__main__': 
    mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
    assert np.equal(reverse_matrix(mat),np.array([[9,8,7],[6,5,4],[3,2,1]])).all()