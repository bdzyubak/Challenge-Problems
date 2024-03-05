def twoArrays(k, A, B):
    valid_combination = 'No'
    valid_iters = len(A) + len(B)
    n = 0
    for n in range(valid_iters):
        valid_combination = check_all_elements(k, A, B)
        if valid_combination == 'Yes':
            break
        else:
            if n < len(A):
                A = permute_array(A)
            else:
                B = permute_array(B)

    return valid_combination


def check_all_elements(k, A, B):
    # Check whether each element is >=k 
    # In numpy, this could be vectorized A+B>=k, 
    # but with regular arrays this results in lists being appended
    element_matches = [False] * len(A)
    for i in range(len(A)):
        if A[i] + B[i] >= k:
            element_matches[i] = True
    if all(element_matches):
        valid_combination = 'Yes'
    else:
        valid_combination = 'No'
    return valid_combination


def permute_array(array):
    # Shift first element to last
    first_val = array.pop()
    return array + [first_val]


if __name__ == '__main__':
    return_value = twoArrays(1, [0, 1], [2, 0])
    print(return_value)
    return_value = twoArrays(1, [2, 1, 3], [7, 8, 9])
    print(return_value)
