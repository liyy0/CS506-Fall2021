import numpy as np



def get_determinant(matrix:np.array):
    if len(matrix) != len(matrix[0]):
        raise ValueError("input matrix size wrong")
    det = 0 
    if len(matrix) == 2:
        det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    else:
        for i in range(len(matrix)):
            newmatrix = np.delete(matrix,0,axis = 0)
            print(i,"-------------------")
            print(newmatrix)
            newmatrix = np.delete(newmatrix,i,axis = 1)
            print(newmatrix)
            det += matrix[0][i]*((-1)**i)*get_determinant(newmatrix)
    return det



