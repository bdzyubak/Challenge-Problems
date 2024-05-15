"""

    A game grid represents water and land masses. The grid contains a True
    value where it's water and False where it's land.
    A boat can go to the next tile in the left or right directions, or move
    twice in the top and bottom directions. All the tiles in the path must be
    inside the grid and contain water.
    Implement the can_travel_to function, which accepts a grid matrix, starting
    and destination coordinates (row and column), and returns a boolean
    indicating whether a boat can travel between the two points in one step.

    For example, the following code:

    game matrix = [
        [False, False, True, True, False],
        [False, False, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, False],
        [False, False, True, False, False]
    ]

    print(can_travel_to (game_matrix, 2, 2, 0, 2))
    print(can_travel_to (game_matrix, 2, 2, 2, 1))
    print(can_travel_to (game_matrix, 2, 2, 2, 3))
    print(can_travel_to(game_matrix, 2, 2, 4, 2))

    Should print:

    True
    False
    True
    False

"""

class BoatMovements:
    def __init__(self, board, start_row, start_column, target_row, target_column):
        self.board = board
        self.seen = [[False] * len(board[0])] * len(board)  # Note, this will set entire row to same value due to pass by reference
        self.seen = [
            [False for _ in range(len(board[0]))]
            for _ in range(len(board))
        ]
        self.target_row = target_row
        self.target_column = target_column

    def valid_move(self, row, column):
        row_in_bounds = 0 <= row < (len(self.board))
        column_in_bounds = 0 <= column < (len(self.board[0]))
        if not row_in_bounds or not column_in_bounds:
            return False

        possible_and_new = (self.board[row][column] is True and
                            self.seen[row][column] is False)
        if not possible_and_new:
            return False
        return True

    # def valid_move(self, row, column):
    #     if 0 <= row < len(self.board) and 0 <= column < len(self.board[0]):
    #         if self.board[row][column] and not self.seen[row][column]:
    #             return True
    #     return False

    def dfs(self, row, column):
        if not self.valid_move(row, column):
            return False

        if row == self.target_row and column == self.target_column:
            return True

        self.seen[row][column] = True
        print(f"{row} {column}")
        return (self.dfs(row + 1, column) or self.dfs(row - 1, column) or
                self.dfs(row, column + 1) or self.dfs(row, column - 1))


def can_travel_to(game_matrix, sx, sy, fx, fy):
    if fx < 0 or fx > (len(game_matrix) - 1) or fy < 0 or fy > (len(game_matrix[0]) - 1):
        return False

    if not game_matrix[sx][sy] or not game_matrix[fx][fy]:
        return False

    game = BoatMovements(board=game_matrix, start_row=sx, start_column=sy, target_row=fx, target_column=fy)

    return game.dfs(sx, sy)


game_matrix = [
        [False, True,  True,  False, False, False],
        [True,  True,  True,  False, False, False],
        [True,  True,  True,  True,  True,  True],
        [False, True,  True,  False, True,  True],
        [False, True,  True,  True,  False, True],
        [False, False, False, False, False, False],
    ]


print(can_travel_to(game_matrix, 3, 2, 2, 2))  # True, Valid move
print(can_travel_to(game_matrix, 3, 2, 3, 4))  # False, Can't travel through land
print(can_travel_to(game_matrix, 3, 2, 6, 2))  # False, Out of bounds

