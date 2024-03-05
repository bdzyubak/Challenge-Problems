arr = [2, 3, 4, 10, 40]
x_exact = {2: 0, 3: 1, 10: 3, 40: 4, 50: ''}
x_nonexact = {0: 0, 2: 0, 3: 1, 3.5: 2, 10: 3, 40: 4, 50: 5}


def test_search_exact(fun):
    for value in x_exact:
        result = fun(arr, value)
        expected = x_exact[value]
        assert result == expected, 'Value ' + str(value) + ' found in position ' + str(result) + ' instead of ' + str(
            expected)


def test_search_nonexact(fun):
    for value in x_nonexact:
        result = fun(arr, value)
        expected = x_nonexact[value]
        assert result == expected, 'Value ' + str(value) + ' found in position ' + str(result) + ' instead of ' + str(
            expected)


def binary_search_recursive(arr, x):
    # print('Testing value: ' + str(x))
    index = bin_search_rec(arr, x, 0, len(arr) - 1)
    return index


def bin_search_rec(arr, x, low, high):
    mid = (high + low) // 2  # middle of (sub)-array
    # print(mid)
    if low > high:
        return ''
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        index = bin_search_rec(arr, x, low, mid - 1)  # Search mid point to the left
    elif arr[mid] < x:
        index = bin_search_rec(arr, x, mid + 1, high)
    return index


def binary_search_recursive_nonexact(arr, x):
    index = bin_search_rec_nonexact(arr, x, 0, len(arr))
    return index


def bin_search_rec_nonexact(arr, x, low, high):
    mid = (high + low) // 2  # middle of (sub)-array
    if low >= len(arr):
        return len(arr)
    elif high <= 0:
        return 0
    elif low > high:
        return low

    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        index = bin_search_rec_nonexact(arr, x, low, mid - 1)  # Search mid point to the left
    elif arr[mid] < x:
        index = bin_search_rec_nonexact(arr, x, mid + 1, high)

    return index


def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
    # Number not in array - return empty
    return ''


def binary_search_iterative_nonexact(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1

    if low >= len(arr):
        return len(arr)
    elif high <= 0:
        return 0
    else:
        # Digit is in the middle of the array but not equal to left or right members
        # Per while loop above, low has exceeded high - same as max(low,high). Return 
        # index that is after the member that that the input is greater than. 
        return low

    # def bin_search_rec_nonexact(arr,x,low,high):


#     if low<high:
#         mid = (low + high) // 2
#         if arr[mid] == x: 
#             return mid 
#         elif arr[mid] > x: 
#             index = bin_search_rec_nonexact(arr,x,low,mid-1)
#         elif arr[mid] < x: 
#             index = bin_search_rec_nonexact(arr,x,mid+1,high)

#     # Reached edge with no match
#     if low == len(arr)-1: 
#         return len(arr)
#     if high == 0: 
#         return 0

#     # Middle of array, no match
#     if arr[index] > x: 
#         return index -1
#     elif arr[index] < x: 
#         return index

if __name__ == '__main__':
    print('Doing exact recursive test.')
    fun = binary_search_recursive
    test_search_exact(fun)

    print('Doing non-exact recursive test.')
    fun = binary_search_recursive_nonexact
    test_search_nonexact(fun)

    print('Doing exact iterative test.')
    fun = binary_search_iterative
    test_search_exact(fun)

    print('Doing non-exact iterative test.')
    fun = binary_search_iterative_nonexact
    test_search_nonexact(fun)
    print('Tests passed.')

# test_search_exact() 

# test_search_nonexact() 
# print('Done.')
