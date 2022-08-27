
def binary_search_recursive(arr,x): 
    mid = search_binary_recursive(arr,x,0,len(arr)-1)
    return mid

def search_binary_recursive(arr,x,low,high): 
    if len(arr) == 1: 
        return 0
    
    if low >= high: 
        return low

    mid = (low + high) // 2
    print(mid)
    if arr[mid] == x: 
        return mid
    elif arr[mid] < x: 
        return search_binary_recursive(arr,x,mid+1,high)
    elif arr[mid] > x: 
        return search_binary_recursive(arr,x,low,mid-1)

def binary_search_nonexact_iterative(arr,x): 
    if len(arr) == 1: 
        return 0
    
    low = 0
    high = len(arr)-1
    mid = (low + high) // 2

    while low<=high: 
        # print(mid)
        if arr[mid] == x: 
            return mid
        elif arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
        mid = (low + high) // 2
    
    if mid <= 0: 
        return 0
    if mid >= (len(arr)-1): 
        return len(arr)
    else: 
        if arr[mid] > x: 
            return mid - 1
        else: 
            return mid + 1

arr = [ 2, 3, 4, 10, 40 ]
# Iterative 
x = 15
result = binary_search_nonexact_iterative(arr,x)
assert result == 4

x = 1
result = binary_search_nonexact_iterative(arr,x)
assert result == 0

x = 2
result = binary_search_nonexact_iterative(arr,x)
assert result == 0

x = 45
result = binary_search_nonexact_iterative(arr,x)
assert result == 5

# Recursive 
x = 15
result = binary_search_recursive(arr,x)
assert result == 4

x = 1
result = binary_search_recursive(arr,x)
assert result == 0

x = 2
result = binary_search_recursive(arr,x)
assert result == 0

x = 45
result = binary_search_recursive(arr,x)
assert result == 5
print('Done.')

























































def binary_search(arr,x): 
    low = 0
    high = len(arr) - 1

    while high>= low: 
        mid = (high+low) //2
        if x > arr[mid]: 
            low = mid + 1
        elif x < arr[mid]: 
            high = mid - 1
        else: 
            return mid
        print(str(low) + ' ' + str(mid) + ' ' + str(high))
    # Index not found
    return -1 


if __name__ == '__main__': 
    # Test array
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10
    
    # Function call
    result = binary_search(arr,x)
    assert result == 3
    print('Done.')







# def binary_search(array,value): 
#     return binary_search_resursive(array,value,min_ind=0,max_ind=len(array)-1)

# def binary_search_resursive(arr, x, min_ind, max_ind):
#     if min_ind < 0: 
#         return 0
#     elif max_ind > len(arr)-1: 
#         return len(arr)
 
#     mid = (max_ind + min_ind) // 2

#     # If element is present at the middle itself
#     if arr[mid] == x:
#         return mid

#     # If element is smaller than mid, then it can only
#     # be present in left subarray
#     elif arr[mid] > x:
#         return binary_search_resursive(arr, x, min_ind, mid - 1)

#     # Else the element can only be present in right subarray
#     else:
#         return binary_search_resursive(arr, x, mid + 1, max_ind) 