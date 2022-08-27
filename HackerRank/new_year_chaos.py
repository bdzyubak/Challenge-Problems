

def chaos(q): 
    # print('New Example:') 
    q = [n-1 for n in q] # Shift original positions to zero-index
    # print(q)
    counter = 0
    for i,value in enumerate(q):
        q_diff = value - i
        if q_diff > 2: 
            return_val = 'Too chaotic'
            print(return_val)
            return return_val
        for j in q[max(value-1,0):i]: 
            if j > value: 
                counter += 1
        # print('Index, value, coutner: ' + str(i) + ' ' + str(value) + ' ' + str(counter))
    
    return_val = counter
    print(return_val)
    return return_val

# def chaos(q): 
#     bribes = 0

#     for i, value in enumerate(q):
#         ind = i+1
#         q_diff = value - ind

#         if q_diff > 2:
#             return "Too chaotic"
        
#         for j in q[max(value - 2, 0):i]:
#             if j > value:
#                 bribes += 1

#     return bribes


if __name__ == '__main__': 
    q = [1,2,3,5,4,6,7,8]
    assert chaos(q) == 1

    q = [4,1,2,3]
    assert chaos(q) == 'Too chaotic'
    
    q = [5, 1, 2, 3, 7, 8, 6, 4]
    assert chaos(q) == 'Too chaotic'

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    assert chaos(q) == 7
    print('Done.')

