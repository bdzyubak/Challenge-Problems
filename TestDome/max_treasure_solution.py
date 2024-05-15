# Treasure hunter. Tiles with treasure have that number of treasures. 0's must be avoided, any negatives should return -1


def max_treasure(treasure_map):
    if not treasure_map or not treasure_map[0]:
        return 0

    def dfs(row, col, v):
        seen.add((row, col))
        dp[row][col] = max(dp[row][col], v)
        for a, b in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
            if 0 <= a < x and 0 <= b < y and treasure_map[a][b] and (a, b) not in seen:
                dfs(a, b, v + treasure_map[a][b])
        seen.discard((i, j))

    x = len(treasure_map)
    y = len(treasure_map[0])
    dp = [[0] * y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if treasure_map[i][j] < 0:
                return -1
            if treasure_map[i][j]:
                seen = set()
                dfs(i, j, treasure_map[i][j])
    return max(c for row in dp for c in row)


treasure_map = [[3, 0, 0, 1, 2],
                [0, 1, 4, 0, 0],
                [5, 0, 0, 3, 3]]
assert max_treasure(treasure_map) == 6

treasure_map = [[3, 0, 0, 1, 2],
                [0, 1, 4, 0, 0],
                [5, 0, 0, 3, 0]]
assert max_treasure(treasure_map) == 5
