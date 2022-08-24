def equalStacks(h1, h2, h3):
    stack_heights = measure_all_heights(h1, h2, h3)
    print(stack_heights)
    while all(stack_heights) and max(stack_heights)>min(stack_heights): 
        print(stack_heights)
        ind = stack_heights.index(max(stack_heights))
        if ind == 0: 
            height_removed = h1.pop(0)
        elif ind == 1: 
            height_removed = h2.pop(0)
        elif ind == 2: 
            height_removed = h3.pop(0)
        stack_heights[ind] -= height_removed
    if not any(stack_heights): 
        return 0
    return min(stack_heights)

def measure_all_heights(h1, h2, h3): 
    height1 = measure_height(h1)
    height2 = measure_height(h2)
    height3 = measure_height(h3)
    return [height1,height2,height3]
    

def measure_height(h): 
    height = 0
    for i in range(len(h)): 
        height+= h[i]
    return height

if __name__ == '__main__': 
    h1 = [1,2,1,1]
    h2 = [1,1,2]
    h3 = [1,1]
    assert equalStacks(h1, h2, h3) == 2

    h1 = [3,2,1,1,1]
    h2 = [4,3,2]
    h3 = [1,1,4,1]
    assert equalStacks(h1, h2, h3) == 5
    print('Done.')