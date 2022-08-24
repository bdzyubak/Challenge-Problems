import re 
import string

def diagonalDifference(arr):
    # Number of diagonals equals the rows. Matrix has to be square
    sum_diag_left = sum_diag(arr,left_right='left')
    sum_diag_right = sum_diag(arr,left_right='right')
    return abs(sum_diag_left-sum_diag_right)

def sum_diag(arr,left_right): 
    sum_diag = 0
    for i in range(len(arr)): 
        if left_right == 'left': 
            row = i
            col = i
        else: 
            row = i
            col = (len(arr)-1)-i
        sum_diag += arr[row][col]
    return sum_diag

if __name__ == '__main__': 
    input = [[11, 2, 4],[4, 5, 6],[10, 8, -12]] 
    assert diagonalDifference(input) == 15 

    input = 0
    assert diagonalDifference(input) == 4294967294 

    input = 1
    assert diagonalDifference(input) == 4294967295
    
