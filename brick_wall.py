def smallest_cut(input):
    current_indeces = [0] * (len(input))
    rolling_sums = [0] * (len(input))
    rolling_pops = list()
    ind = 0
    while any(input):
        row_pops = 0
        for row in range(len(input)):
            if rolling_sums[row] <= ind:
                rolling_sums[row] += input[row].pop(0)
                current_indeces[row] += 1
                row_pops += 1
            # print(rolling_sums)
            # print(current_indeces)
        rolling_pops.append(row_pops)
        ind += 1
    # print(rolling_pops)
    # Max number of pops (advancing to next brick) is equivalent to smallest number of cuts
    # Skip first entry which is all bricks starting at the edge
    index_of_smallest_cut = rolling_pops.index(max(rolling_pops[1:]))
    smallest_cut = rolling_sums[0] - max(rolling_pops[1:])
    return smallest_cut


if __name__ == '__main__':
    input = [[1, 2, 2, 1],
             [3, 1, 2],
             [1, 3, 2],
             [2, 4],
             [3, 1, 2],
             [1, 3, 1, 1]]

    assert smallest_cut(input) == 2
