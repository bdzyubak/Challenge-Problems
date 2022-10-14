
from tictac import Game
import numpy as np
from copy import deepcopy
import pytest

height = 3
width = 4
game = Game()
board = np.zeros((height,width,2))
result_board = game.print_board()


row = 0
col = 1
index = 1
position_mask = np.zeros_like(board)
position_mask[row,col,index] = 1
game.make_move(position_mask)
game.print_board()
# def test_new(): 
#     result_board = game.print_board()
    
    # assert result_board == board, 'Failed to make original board.'

def test_position_mask_to_coord(): 
    row = 0
    col = 1
    index = 0
    position_mask = np.zeros_like(board)
    position_mask[row,col,index] = 1
    r,c,i = game.position_mask_to_coord(position_mask)
    assert [r,c,i] == [row,col,index], 'Failed to fetch position.'

    row = 1
    col = 2
    index = 1
    position_mask = np.zeros_like(board)
    position_mask[row,col,index] = 1
    r,c,i = game.position_mask_to_coord(position_mask)
    assert [r,c,i] == [row,col,index], 'Failed to fetch position.'

def test_check_end(): 
    image = np.zeros((5,5))
    assert game.check_end(image) == False, 'Failed to continue incomplete image.'
    
    image[:,1] = 1
    assert game.check_end(image) == True, 'Failed to stop complete image.' 

    game.board = np.zeros((5,5,2))
    assert game.check_end_both() == False, 'Failed to continue incomplete game.'

    game.board[:,1,0] = 1
    assert game.check_end_both() == 0, 'Failed to identify index 0 as complete.'
    
    game.board = np.zeros((5,5,2))
    game.board[:,1,1] = 1
    assert game.check_end_both() == 1, 'Failed to identify index 1 as complete.'

if __name__ == '__main__': 
    pytest.main()
