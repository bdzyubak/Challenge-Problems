def grid_challenge(grid): 
    grid_out = [None] * len(grid)
    for i, row in enumerate(grid): 
        row_out, was_sorted = alphabetic_arrange(row)
        grid_out[i] = row_out
    # print(grid_out) 
    columns_sorted = list()
    for s in range(len(row)): 
        column = make_colummn(grid_out,s)
        _, was_sorted = alphabetic_arrange(column)
        columns_sorted.append(was_sorted)
        print(column)
    
    if all(columns_sorted): 
        return_message = 'YES'
    else: 
        return_message = 'NO'
    print(return_message)
    return return_message

def alphabetic_arrange(row): 
    row_out = "".join(sorted(row))
    was_sorted = row == row_out
    return row_out, was_sorted

def make_colummn(grid,ind): 
    column = ''
    for row in grid: 
        column += row[ind]
    return column

if __name__ == '__main__': 
    grid = ['abc','ade','efg']
    assert grid_challenge(grid) == 'YES'

    grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    assert grid_challenge(grid) == 'YES'