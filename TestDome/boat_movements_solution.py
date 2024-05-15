class BoatMovements:
    def __init__(self, matrix, to_row, to_column):
        self.row = to_row
        self.column = to_column
        self.matrix = matrix
        self.visited = [
            [False for _ in range(len(matrix[0]))]
            for _ in range(len(matrix))
        ]

    def valid_move(self, row, column):

        if 0 <= row < len(self.matrix) and 0 <= column < len(self.matrix[0]):
            if self.matrix[row][column] and not self.visited[row][column]:
                return True

        return False

    def dfs_search(self, row, column):

        if not self.valid_move(row, column):
            return False

        if self.row == row and self.column == column:
            return True

        self.visited[row][column] = True

        # return (self.dfs_search(row - 1, column) or
        #         self.dfs_search(row, column - 1) or
        #         self.dfs_search(row + 1, column) or
        #         self.dfs_search(row, column + 1))
        print(f"{row} {column}")
        return (self.dfs_search(row + 1, column) or self.dfs_search(row - 1, column) or
                self.dfs_search(row, column + 1) or self.dfs_search(row, column - 1))


def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):

    try:
        # Check that:
        # 1- the given coordinates within the grid.
        # 2- the start and end coordinates is True.
        # 3- restrict the moves (two top/down and one left/right).
        if (to_row > len(game_matrix) - 1) or \
           (to_column > len(game_matrix) - 1) or \
           not game_matrix[from_row][from_column] or \
           not game_matrix[to_row][to_column] or \
           abs(to_row - from_row) > 2 or \
           abs(to_column - from_column) > 1:
            return False
    except IndexError:
        raise IndexError("The indexes must be valid indexes!")

    boat_movements = BoatMovements(game_matrix, to_row, to_column)
    return boat_movements.dfs_search(from_row, from_column)


# game_matrix = [
#         [False, False, True, True, False],
#         [False, False, True, False, False],
#         [False, False, True, True, False],
#         [False, True, False, True, False],
#         [False, False, True, False, False]
# ]
#
# print(can_travel_to(game_matrix, 2, 2, 0, 2))
# print(can_travel_to(game_matrix, 2, 2, 2, 1))
# print(can_travel_to(game_matrix, 2, 2, 2, 3))
# print(can_travel_to(game_matrix, 2, 2, 1, 2))

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
