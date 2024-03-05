#               1
#             /   \
#           2       6
#         /   \      \
#       3       4 --> 5

graph = {
    1: [2, 6],
    2: [3, 4],
    3: [],
    4: [5],
    5: [],
    6: [5]
}


def depth_first_search(graph, node):
    return


def breadth_first_search(graph, node):
    return


if __name__ == '__main__':
    print('Testing depth first search.')
    assert depth_first_search(graph, 1) == [1, 2, 3, 4, 5, 6], 'Depth first search not correct for node 1.'

    print('Testing breadth first search.')
    assert breadth_first_search(graph, 1) == [1, 2, 6, 3, 4, 5], 'Breadth first search not correct for node 1.'
    print('Tests passed.')
