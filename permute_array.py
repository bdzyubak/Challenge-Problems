import itertools


def permute_rec(arr):
    if len(arr) <= 1:
        return [arr]
    permutations = list()
    for i in range(len(arr)):
        for perm in permute_rec(arr[:i] + arr[i + 1:]):
            permutations.append([arr[i]] + perm)
    return permutations


# def permute_iter(arr):
#     if len(arr) <= 1: 
#         return [arr]
#     permutations = list()
#     permutations.append(arr[0])
#     for i in range(1,len(arr)): 
#         for j in reversed(range(len(permutations))): 
#             curr = permutations.pop(j)
#             for k in range(len(curr)+1): 
#                 permutations.append(permutations[:k] + arr[i] + permutations[k:])
#     return permutations


def test_permute(fun, arr):
    iter_permuted_tuples = list(itertools.permutations(arr))
    iter_permuted = [list(name) for name in iter_permuted_tuples]
    fun_permuted = fun(arr)
    print('Array:')
    print(arr)
    print('System permutations:')

    print(iter_permuted)
    print('Answer permutations:')
    print(fun_permuted)
    same_size = len(fun_permuted) == len(iter_permuted)
    all_elements = all(element in iter_permuted for element in fun_permuted)
    assert (same_size and all_elements) == True, 'Array does not match system answer.'


if __name__ == '__main__':
    arr = [1, 2, 3]
    fun = permute_rec
    test_permute(fun, arr)

    arr = [1, 5, 7, 3, 2]
    fun = permute_rec
    test_permute(fun, arr)

    # arr = [1,2,3]
    # fun = permute_iter
    # test_permute(fun,arr)

    # arr = [1,5,7,3,2]
    # fun = permute_iter
    # test_permute(fun,arr)
    print('Tests passed.')
