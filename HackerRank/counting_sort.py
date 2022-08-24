import re 
import string

def counting_sort(arr):
    array_range = (max(arr) - min(arr))+1
    count_array = [0]*array_range
    for value in arr: 
        count_array[value-min(arr)] +=1
    return count_array

# Assuming values are all in 0-100 range as per HackerRank
def countingSort_0_100(arr):    
    array_range = 100
    count_array = [0]*array_range
    for value in arr: 
        count_array[value] +=1
    return count_array

if __name__ == '__main__': 
    input = [2,3,4] 
    assert counting_sort(input) == [1,1,1]
    
    input = [3,4,5,1,1,2,5,5,6] 
    assert counting_sort(input) == [2,1,1,1,3,1]

    input = [-1,3,4] 
    assert counting_sort(input) == [1,0,0,0,1,1]
