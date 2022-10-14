import numpy as np

class Game(): 
    def __init__(self,height=3,width=3,run_length=3): 
        if not height == width == run_length: 
            raise(ValueError('Currently limited to height=widht=run_length'))
        self.height = height
        self.width = width
        self.run_length = run_length
        self.make_new_board()
        # self.print_board()

    def make_new_board(self): 
        # One hot encoded board
        self.board = np.zeros((self.height,self.width,2))

    def print_board(self,alternative_board=''): 
        print('')
        board = self.board if not alternative_board else alternative_board
        for i in range(self.height): 
            row_string = ''
            for j in range(self.width): 
                placement_value = np.argwhere(board[i,j])
                if len(placement_value)>1: 
                    raise(ValueError('Board has multiple labels at location: ' + str(i) + ' ' + str(j)))
                elif not placement_value: 
                    row_string += '.'
                elif placement_value == 0: 
                    row_string += 'O'
                elif placement_value == 1: 
                    row_string += 'X'
            print(row_string)
        print('')
        return board

    def make_move(self,position_mask): 
        row,col,index = self.position_mask_to_coord(position_mask)
        self.board[row,col,index] = 1

    # def make_position_mask(self,row,col): 
    #     if np.max(self.board[row,col])>0: 
    #         raise(ValueError('Location row: ' + str(row) + ' col: ' + str(col) + ' already occupied.'))
    #     position_mask = np.zeros_like(self.board)
    #     position_mask[row,col] = 1
    #     return position_mask
    
    def position_mask_to_coord(self,position_mask): 
        if np.sum(position_mask)!=1: 
            raise(ValueError('Position mask must have exactly one non-zero marker.'))
        position_coords = np.argwhere(position_mask)[0]
        row = position_coords[0]
        col = position_coords[1]
        index = position_coords[2]
        return row, col, index

    def check_end_both(self): 
        for index in [0,1]: 
            if self.check_end(np.squeeze(self.board[:,:,index])): return index 
        return False

    def check_end(self,board): 
        rows = [np.squeeze(board[i,:]) for i in range(board.shape[0])]
        cols = [np.squeeze(board[:,j]) for j in range(board.shape[1])]
        diags_right = [[np.squeeze(board[i,i]) for i in range(board.shape[0])]]
        # diags_right = [diag for diag in diags_right if len(diag)>=self.run_length]
        diags_left = [[np.squeeze(board[board.shape[0]-i-1,i]) for i in range(board.shape[0])]]
        # diags_left = [diag for diag in diags_left if len(diag)>=self.run_length]
    
        if self.check_run(rows): return True
        if self.check_run(cols): return True
        if self.check_run(diags_right): return True
        if self.check_run(diags_left): return True
        return False
    

    def check_run(self,runs): 
        for run in runs: 
            length = 0
            for value in run: 
                if value>0: 
                    length +=1
                    if length>=self.run_length: 
                        return True
                else: 
                    length = 0
        return False


# class Game(): 
#     def __init__(self,height=3,width=4): 
#         self.height = height
#         self.width = width
#         self.make_new_board()
#         self.print_board()

#     def make_new_board(self): 
#         self.board = []
#         for i in range(self.height): 
#             self.board.append(['.']*self.width)

#     def print_board(self): 
#         for i in range(self.height): 
#             row_string = ''
#             for j in range(self.width): 
#                 row_string += self.board[i][j]
#             print(row_string)
#         return self.board

# def encode_state(self,state): 
#     state_encode = 0
#     power = 0
#     for i in len(state): 
#         state_encode+=state[i]*3**power
#         power+=1
#     return state_encode

# def decode_state(self,state_encode): 
#     power = 0
#     current_value = 0
    
#     for i in range(self.height):     
#         decoded_row = []
#         for j in range(self.width): 
#             decoded_row.append()