####################################################################################################
# Interview task to implement basic linear algebra operations and speed them up
# 
# Bogdan Dzyubak 04/14/2022
# illan7@gmail.com
####################################################################################################
import numpy as np

def element_wise_multiplication(M1,M2): 
    if M1.shape != M2.shape: 
        raise(ValueError('Matrix sizes not equal.'))

    M_out = np.zeros_like(M1)
    for i in range(M1.shape[0]): 
        for j in range(M1.shape[1]): 
            M_out[i,j] = M1[i,j] * M2[i,j]
    return M_out


def matrix_multiply_basic(M,N): 
    if M.shape[1] != N.shape[0]: 
        raise(ValueError('Matrix innder dimensions must agree.'))
    M_out = np.zeros((M.shape[0],N.shape[1])) # mxn multiplied with nx1 is mx1
    for i in range(M.shape[0]): 
        for j in range(M.shape[1]): 
            for k in range(N.shape[1]):
                M_out[i,k] += M[i,j]*N[j,k]

    return M_out
