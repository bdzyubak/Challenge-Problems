
arr = [ 2, 3, 4, 10, 40 ]
# x_exact = {2:0, 3:1, 10:3 ,40:4, 50:''}
x_nonexact = {0:0, 2:0, 3:1, 3.5:2, 10:3 ,40:4, 30:4, 50:5}

def test_search_nonexact(fun): 
    for value in x_nonexact: 
        result = fun(arr,value)
        expected = x_nonexact[value]
        assert result == expected, 'Value ' + str(value) + ' found in position ' + str(result) + ' instead of ' + str(expected)



def binary_search_nonexact_iterative(arr,x):    
    return

if __name__ == '__main__': 
    print('Doing non-exact iterative test.')
    fun = binary_search_nonexact_iterative
    test_search_nonexact(fun)
    print('Tests passed.')
