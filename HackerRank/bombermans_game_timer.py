def bomberMan(n,grid): 
    print('State after ' + str(n) + ' seconds.')
    rows, columns = get_grid_dims(grid)
    grid_counter = list()
    for c in range(columns): 
        grid_counter.append([0]*rows)
    grid, grid_counter = advance_counter(grid,grid_counter,rows,columns) # STEP 2 - wait one second
    for time in range(2,n+1): 
        if time % 2 == 0: 
            grid, grid_counter = plant_empty(grid,grid_counter,rows,columns) # STEP 3 - place in empty
        else: 
            grid = clear_placed(grid,grid_counter,rows,columns)
    print_grid(grid)
    print_grid(grid_counter)
    print()
    return grid 

def advance_counter(grid,grid_counter,rows,columns): 
    for r in range(rows): 
        for c in range(columns): 
            if grid[r][c] == 'O': 
                grid_counter[r][c] = grid_counter[r][c] + 1
    return grid, grid_counter

def plant_empty(grid,grid_counter,rows,columns): 
    grid, grid_counter = advance_counter(grid,grid_counter,rows,columns) 
    for r in range(rows): 
        for c in range(columns): 
            if grid[r][c] == '.': 
                grid, grid_counter = set_tile(grid,grid_counter,r,c,'O')
    return grid, grid_counter

def clear_placed(grid,grid_counter,columns,rows): 
    grid, grid_counter = advance_counter(grid,grid_counter,rows,columns) 
    for r in range(rows): 
        for c in range(columns): 
            if grid[r][c] == 'O' and grid_counter[r][c]>=3: 
                grid,grid_counter = clear_neighbors(grid,grid_counter,r,c)
    return grid

def clear_neighbors(grid,grid_counter,r,c): 
    for i in [-1,1]: 
        for j in [-1,1]: 
            ind_row = r+j
            ind_column = c+i
            in_bounds = (ind_row> 0 and ind_row < get_grid_dims(grid)[0]) \
                            and (ind_column>=0 and ind_column < len(grid))
            if not in_bounds: 
                continue
            grid, grid_counter = set_tile(grid,grid_counter,ind_row,ind_column,'.')
    return grid, grid_counter

def get_grid_dims(grid): 
    rows = len(grid)
    columns = len(grid[0])
    return rows, columns

def set_tile(grid,grid_counter,r,c,type): 
    grid[r][c] = type
    grid_counter[r][c] = 0
    return grid, grid_counter

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