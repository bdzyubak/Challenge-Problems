import itertools

def permute_rec(arr): 
    pass

# def permute_iter(arr): 
#     pass
    

def test_permute(fun,arr): 
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
    arr = [1,2,3]
    fun = permute_rec
    test_permute(fun,arr)
    
    arr = [1,5,7,3,2]
    fun = permute_rec
    test_permute(fun,arr)

    # arr = [1,2,3]
    # fun = permute_iter
    # test_permute(fun,arr)
    
    # arr = [1,5,7,3,2]
    # fun = permute_iter
    # test_permute(fun,arr)
    print('Tests passed.')
