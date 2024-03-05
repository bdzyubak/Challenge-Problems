####################################################################################################
# Unit tests for task to implement basic linear algebra operations and speed them up
# 
# Bogdan Dzyubak 04/14/2022
# illan7@gmail.com
####################################################################################################

import numpy as np
from matrix_operations import element_wise_multiplication, matrix_multiply_basic
import pytest

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
N = np.array([[10, 20], [30, 40], [50, 60]])
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])


def test_vstack():
    M1 = np.vstack([v1, v2, v3])
    assert np.array_equal(M1, M), 'Virtical stacking not working'


def test_elementwise_multiplication():
    # Element wise multiplication 
    M_out = element_wise_multiplication(M, M)
    assert np.array_equiv(M_out, M * M), 'Element wise multiplication error'
    # Explicit check for matrix equal if all elements equal
    assert np.equal(M_out, np.multiply(M, M)).all(), 'Element wise multiplication error'


def test_broadcasting():
    # Broadcasting to higher dimensinality not implemented
    with pytest.raises(ValueError) as e_info:
        element_wise_multiplication(M, v1)


def test_matrix_multiplication():
    # Matrix multiplication
    M_out = matrix_multiply_basic(M, N)
    assert np.array_equiv(M_out, np.matmul(M, N)), 'Matrix by matrix multiplication error'


if __name__ == "__main__":
    retcode = pytest.main()
