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
    visited = list()
    return dfs(visited, graph, node)


def dfs(visited, graph, node):  # Depth first search
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited


def breadth_first_search(graph, node):
    visited = list()
    queue = list()
    visited.append(node)
    queue.append(node)
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return visited


if __name__ == '__main__':
    print('Testing depth first search.')
    assert depth_first_search(graph, 1) == [1, 2, 3, 4, 5, 6], 'Depth first search not correct for node 1.'

    print('Testing breadth first search.')
    assert breadth_first_search(graph, 1) == [1, 2, 6, 3, 4, 5], 'Breadth first search not correct for node 1.'
    print('Tests passed.')
