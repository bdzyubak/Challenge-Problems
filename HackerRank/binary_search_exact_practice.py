
arr = [ 2, 3, 4, 10, 40 ]
x_exact = {2:0, 3:1, 10:3 ,40:4, 50:''}
def test_search_exact(fun): 
    for value in x_exact: 
        result = fun(arr,value)
        expected = x_exact[value]
        assert result == expected, 'Value ' + str(value) + ' found in position ' + str(result) + ' instead of ' + str(expected)

def binary_search_recursive(arr,x): 
    index = bin_search_rec(arr,x,0,len(arr)-1)
    return index

def bin_search_rec(arr,x,low,high): 
    pass

def binary_search_iterative(arr,x): 
    pass

if __name__ == '__main__': 
    
    print('Doing exact recursive test.')
    fun = binary_search_recursive
    test_search_exact(fun)

    print('Doing exact iterative test.')
    fun = binary_search_iterative
    test_search_exact(fun)

    print('Tests passed.')

