
arr = [ 2, 3, 4, 10, 40 ]
x_exact = {2:0, 3:1, 10:3 ,40:4, 50:''}
x_inexact = {0:0, 2:0, 3:1, 3.5:2, 10:3 ,40:4, 50:5}

def test_search_exact(): 
    print('Doing exact iterative test.')
    for value in x_exact: 
        result = binary_search_iterative(arr,value)
        expected = x_exact[value]
        assert result == expected, 'Value ' + str(value) + ' found in position ' + str(result) + ' instead of ' + str(expected)
    
    # print('Doing exact recursive test.')
    # for value in x_exact: 
    #     assert binary_search_recursive(arr,value) == x_exact[value], 'Value ' + str(value) + ' not found in position ' + str(x_exact[value])

def test_search_nonexact(): 
    print('Doing nonexact iterative test.')
    for value in x_exact: 
        result = binary_serach_nonexact(arr,value)
        expected = x_inexact[value]
        assert result == expected, 'Value ' + str(value) + ' found in position ' + str(result) + ' instead of ' + str(expected)
    
    # print('Doing inexact recursive test.')
    # for value in x_exact: 
    #     assert fun(arr,value) == x_exact[value], 'Value ' + str(value) + ' not found in position ' + str(x_exact[value])

def binary_search_iterative(arr,x): 
    # Assumes ascending order
    low = 0
    high = len(arr)-1
    mid = (low + high) // 2
    while high >= low: 
        if x == arr[mid]: 
            return mid
        elif x < arr[mid]: 
            high = mid-1
        elif x > arr[mid]: 
            low = mid + 1
        mid = (low + high) // 2
    return '' # If not found

def binary_serach_nonexact(arr,x): 
    low = 0
    high = len(arr)-1
    mid = (low + high) // 2
    while high >= low: 
        if x == arr[mid]: 
            return mid
        elif x < arr[mid]: 
            high = mid-1
        elif x > arr[mid]: 
            low = mid + 1
        mid = (low + high) // 2
    
    if low <=0: 
        return 0
    if high >= len(arr): 
        return len(arr)
    if x < arr[mid]: 
        return low - 1
    if x > arr[mid]: 
        return high + 1
    return '' # If not found


test_search_exact() 
test_search_nonexact() 
print('Done.')
