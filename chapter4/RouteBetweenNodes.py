from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self,a,b):
        self.graph[a].append(b)
    
    def is_reachable(self,a,b):
        visited = [a]
        next_nodes = [a]

        while(len(next_nodes)):
            cur = next_nodes.pop(0)

            if cur == b:
                return True
            
            neighbors = self.graph[cur]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    next_nodes.append(neighbor)
        return False

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(g.graph)
    nodes = g.graph.keys()
    for i in nodes:
        for j in nodes:
            print(i,'->',j,':',g.is_reachable(i,j))