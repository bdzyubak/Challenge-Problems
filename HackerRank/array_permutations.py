def two_arrays(k, A, B):
    permutations_A = permute_array(A)
    permutations_B = permute_array(B)
    perms_valid = [False] * len(permutations_A)
    for i in range(len(A)):
        # print(permutations_A[i])
        # print(permutations_B[i])
        # print(k)
        for j in range(len(B)):
            perms_valid.append(check_perm_valid(permutations_A[i], permutations_B[j], k))
    if any(perms_valid):
        valid_combintation_exists = 'YES'
    else:
        valid_combintation_exists = 'NO'
    return valid_combintation_exists


def check_perm_valid(A_perm, B_perm, k):
    perm_ind_valid = [False] * (len(A))
    for h in range(len(A)):
        if A_perm[h] + B_perm[h] >= k:
            perm_ind_valid[h] = True
    if all(perm_ind_valid):
        return True
    else:
        return False


def permute_array(array):
    if len(array) == 0:
        return []

    if len(array) == 1:
        return [array]

    # List of permutations for this subset
    perm = list()
    for i in range(len(array)):
        extract_element = array[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        list_without_element = array[:i] + array[i + 1:]

        for j in permute_array(list_without_element):
            perm.append([extract_element] + j)

    return perm


A = [1, 2, 3]
permutations = permute_array(A)
assert permutations == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], 'Fails to permute an array.'

A = [2, 1, 3]
B = [7, 8, 9]
k = 10
print(two_arrays(k, A, B))
assert two_arrays(k, A, B) == 'YES', 'Fails to detect true positive.'

A = [1, 2, 2, 1]
B = [3, 3, 3, 4]
k = 5
assert two_arrays(k, A, B) == 'NO', 'Fails to reject true negative.'

A = [1, 3]
B = [3, 1]
k = 4
assert two_arrays(k, A, B) == 'YES', 'Fails to detect true positive.'

A = [2, 3, 1, 1, 1]
B = [1, 3, 4, 3, 3]
k = 5
assert two_arrays(k, A, B) == 'NO', 'Fails to reject true negative'

A = [1, 5, 1, 4, 4, 2, 7, 1, 2, 2]
B = [8, 7, 1, 7, 7, 4, 4, 3, 6, 7]
k = 10
assert two_arrays(k, A, B) == 'NO', 'Fails to reject true negative'

A = [3, 6, 8, 5, 9, 9, 4, 8, 4, 7]
B = [5, 1, 0, 1, 6, 4, 1, 7, 4, 3]
k = 9
assert two_arrays(k, A, B) == 'YES', 'Fails to detect true positive.'

A = [4, 4, 3, 2, 1, 4, 4, 3, 2, 4]
B = [2, 3, 0, 1, 1, 3, 1, 0, 0, 2]
k = 4
assert two_arrays(k, A, B) == 'YES', 'Fails to detect true positive.'
