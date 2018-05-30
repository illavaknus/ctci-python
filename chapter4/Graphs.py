def bfs(graph, node):
    visited = []
    next_nodes = [node]
    
    levels = {}
    levels[node] = 0
    
    while len(next_nodes):
        cur = next_nodes.pop(0)
        if cur not in visited:
            visited.append(cur)
        for neighbor in graph[cur]:
            if neighbor not in visited:
                visited.append(neighbor)
                next_nodes.append(neighbor)
                levels[neighbor] = levels[cur]+1
    return visited,levels



def dfs(graph,node,visited=[]):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
    return visited

if __name__ == '__main__':
    # sample graph implemented as a dictionary
    graphs = [
        {
            'root': 'A',
            'A': ['B', 'C', 'E'],
            'B': ['A','D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B'],
            'E': ['A', 'B','D'],
            'F': ['C'],
            'G': ['C']
        },
        {
            'root': 'A',
            'A' : ['B','S'],
            'B' : ['A'],
            'C' : ['D','E','F','S'],
            'D' : ['C'],
            'E' : ['C','H'],
            'F' : ['C','G'],
            'G' : ['F','S'],
            'H' : ['E','G'],
            'S' : ['A','C','G']
        }
    ]

    for graph in graphs:
        print('\nDFS:',dfs(graph,graph['root']))
        bfs_sequence = bfs(graph,graph['root'])
        print('BFS:',bfs_sequence[0])
        print('Levels:',bfs_sequence[1])