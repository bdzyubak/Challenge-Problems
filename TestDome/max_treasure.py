# Treasure hunter. Tiles with treasure have that number of treasures. 0's must be avoided, any negatives should return -1


def max_treasure(treasure_map):
    if not treasure_map or not treasure_map[0]:
        return 0

    def dfs(row, col):
        if row < 0 or row >= len(treasure_map) or col < 0 or col >= len(treasure_map[0]):
            return 0

        if not treasure_map[row][col] or seen[row][col]:
            return 0

        # print(f"{row} {col} {treasure_map[row][col]}")
        seen[row][col] = True
        instance_treasure = treasure_map[row][col] + max([dfs(row-1, col), dfs(row+1, col),
                                                          dfs(row, col-1), dfs(row, col+1)])
        return instance_treasure

    # # Loop over starting locations
    max_treasure = 0
    for i in range(len(treasure_map)):
        for j in range(len(treasure_map[0])):
            if treasure_map[i][j] < 0:
                return -1
            if treasure_map[i][j]:
                # Re-initialize map of seen places for this start location
                seen = [[False for _ in range(len(treasure_map[0]))] for _ in range(len(treasure_map))]
                max_treasure = max(max_treasure, dfs(i, j))
                # print(f"Start at {i} {j} {max_treasure}")
    # i = 1
    # j = 2
    # seen = [[False for _ in range(len(treasure_map[0]))] for _ in range(len(treasure_map))]
    # max_treasure = max(max_treasure, dfs(i, j))
    # print(f"Start at {i} {j} {max_treasure}")
    return max_treasure


treasure_map = [[3, 0, 0, 1, 2],
                [0, 1, 4, 0, 0],
                [5, 0, 0, 3, 3]]
assert max_treasure(treasure_map) == 6

treasure_map = [[3, 0, 0, 1, 2],
                [0, 1, 4, 0, 0],
                [5, 0, 0, 3, 0]]
assert max_treasure(treasure_map) == 5
