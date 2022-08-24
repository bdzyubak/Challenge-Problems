
def binary_search_recursive(arr,x): 
    return binary_search_subfunct(arr,x,0,len(arr)-1)

def binary_search_subfunct(arr,x,min,max): 
    mid = (min + max) // 2

    if x == arr[mid]: 
        return mid
    elif x < arr[mid]: 
        return binary_search_subfunct(arr,x,min,mid-1)
    elif x > arr[mid]: 
        return binary_search_subfunct(arr,x,mid+1,max)

def binary_search_iterative(arr,x): 
    min = 0
    max = len(arr) - 1
    mid = (min + max) // 2

    while min < max: 
        mid = (min + max) // 2
        # print(str(min) + ' ' + str(max) + ' ' + str(mid))
        if arr[mid] == x: 
            return mid
        elif x < arr[mid]: 
            max = mid - 1
        elif x > arr[mid]: 
            min = mid + 1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search_recursive(arr,x)
assert result == 3

result = binary_search_iterative(arr,x)
assert result == 3
print('Done.')


