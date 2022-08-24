def twoArrays(k,A,B): 
    perm_A = permutations(A)
    perm_B = permutations(B)
    for i in range(len(perm_A)): 
        for j in range(len(perm_B)): 
            valid = 'YES'
            for n in range(len(perm_A[i])): 
                if perm_A[i][n] + perm_B[j][n] < k: 
                    valid = 'NO'
            if valid == 'YES': 
                return valid
    return 'NO'


def permutations(array): 
    if len(array) <=1: 
        return [array]
    perm = []
    for i in range(len(array)): 
        perms = permutations(array[:i] + array[i+1:])
        for p in perms: 
            perm.append([array[i],*p])
    return perm

def test_valid_perm(k,perm_A,perm_B): 
    valid = 'YES'
    for j in range(len(perm_A)): 
        if perm_A[j] + perm_B[j] < k: 
            valid = 'NO'
    return valid

if __name__ == '__main__': 
    A = [1,0]
    B = [0,2]
    k = 1
    assert test_valid_perm(k,A,B) == 'YES'

    A = [0,1]
    B = [0,2]
    k = 1
    assert test_valid_perm(k,A,B) == 'NO'
    
    A = [0,1,2]
    assert permutations(A) == [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    
    A = [1,0]
    B = [0,2]
    k = 1
    assert twoArrays(k,A,B) == 'YES'

    A = [2,1,3]
    B = [7,8,9]
    k = 10
    assert twoArrays(k,A,B) == 'YES'

    A = [1,2,2,1]
    B = [3,3,3,4]
    k = 5
    assert twoArrays(k,A,B) == 'NO'
    print('Done.')