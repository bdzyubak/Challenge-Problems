
def depth_first_search(graph,node): 
    dfs(graph,node,[])

def dfs(graph,node,visited): 
    if node not in visited: 
        visited.append(node)
        


if __name__ == '__main__': 
    graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []}

