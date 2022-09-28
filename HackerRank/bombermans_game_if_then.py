def bomberMan(n,grid): 
    print('State after ' + str(n) + ' seconds.')
    rows, columns = get_grid_dims(grid)
    grid_full = make_full_grid(grid,rows,columns)
    grid_opposite = make_inverted(grid,rows,columns)
    if n <=1 or (n-1) % 4 == 0: 
        return grid
    elif (n-3) % 4 == 0: 
        return grid_opposite
    else: # n % 2 == 0
        return grid_full

def make_full_grid(grid,rows,columns): 
    
    new_grid = list()
    for _ in range(rows): 
        new_grid.append(['O']*columns)
    return new_grid

def make_inverted(grid,rows,columns): 
    new_grid = make_full_grid(grid,rows,columns)
    for row in range(rows): 
        for col in range(columns): 
            neighbors = [grid[row][col],grid[max(row-1,0)][col],grid[min(row+1,rows-1)][col],
                        grid[row][max(col-1,0)],grid[row][min(col+1,columns-1)]]
            if any(elem for elem in neighbors if elem == 'O'): 
                new_grid[row][col] = '.'
    return new_grid

def get_grid_dims(grid): 
    rows = len(grid)
    columns = len(grid[0])
    return rows, columns


def print_grid(grid): 
    for row in grid: 
        print(row)

def make_grid_center(): 
    grid = [['.','.','.'],
            ['.','O','.'],
            ['.','.','.']]
    return grid

def test_bomberMan(): 
    grid = make_grid_center()
    n = 1
    grid_after_n = bomberMan(n,grid)
    grid_after_n_correct = [['.','.','.'],
                            ['.','O','.'],
                            ['.','.','.']]
    assert grid_after_n == grid_after_n_correct

    grid = make_grid_center()
    n = 2
    grid_after_n = bomberMan(n,grid)
    grid_after_n_correct = [['O','O','O'],
                            ['O','O','O'],
                            ['O','O','O']]
    assert grid_after_n == grid_after_n_correct

    grid = make_grid_center()
    n = 3
    grid_after_n = bomberMan(n,grid)
    grid_after_n_correct = [['O','.','O'],
                            ['.','.','.'],
                            ['O','.','O']]
    assert grid_after_n == grid_after_n_correct

# def make_initial(c,r): 
#     mid_r = r // 2
#     mid_c = r // 2
#     game_board = [['.']*c]*r
#     game_board[mid_c,mid_r] = 'O'
#     return game_board

if __name__ == '__main__': 
    test_bomberMan()