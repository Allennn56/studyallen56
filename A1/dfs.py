from collections import defaultdict
 
 
class Graph:
 
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSfun(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited[v] = True 
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
           if visited[i] = False
                self.DFSfun(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        visited = [False]*(len(self.graph))
        
        self.DFSfunc(v, visited)
 
# Driver code
 
 
# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
