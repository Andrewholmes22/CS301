from collections import deque
class AdjacencyMatrix:
    def __init__(self):
        self.graph = []
        self.vertices = []
    def readGraph(self,filepath):
        fi = open(filepath)
        val = fi.readline().split()
        num_Verts = int(val[0])
        num_Edges = int(val[1])
        self.vertices = fi.readline().strip().split(',')
        self.graph = [['0' for _ in range(num_Verts+1)]for _ in range(num_Verts+1)]
        for i in range(1,len(self.vertices)+1):
            self.graph[0][i] = self.vertices[i-1]
            self.graph[i][0] = self.vertices[i-1]
            
        for line in fi:
            numbLine = line.strip().split(' ')
            self.graph[self.vertices.index(numbLine[0])+1][self.vertices.index(numbLine[1])+1] = '1'
            self.graph[self.vertices.index(numbLine[1])+1][self.vertices.index(numbLine[0])+1] = '1'
        fi.close()
        return True
    def addVertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.graph[0].append(vertex)
            for line in self.graph:
                if line[0] == '0':
                    continue
                else:
                    line.append('0')
            self.graph.append([vertex])
            while len(self.graph[-1]) < len(self.vertices)+1:
                self.graph[-1].append('0')
            return True
        else:
            return False
    def addEdge(self,edge):
        if edge[0] in self.graph[0]:
            hor = self.graph[0].index(edge[0])
        else:
            return False
        if edge[1] in self.graph[0]:
            ver = self.graph[0].index(edge[1])
        else:
            return False
        self.graph[hor][ver] = '1'
        self.graph[ver][hor] = '1'
        return True
    def deleteVertex(self,vertex):
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            vert = self.graph[0].index(vertex)
            for line in self.graph:
                line.pop(vert)
            for line in self.graph:
                if line[0] == vertex:
                    self.graph.remove(line)
            return True
        else:
            return False
    def deleteEdge(self,edge):
        if edge[0] in self.graph[0]:
            hor = self.graph[0].index(edge[0])
        else:
            return False
        if edge[1] in self.graph[0]:
            ver = self.graph[0].index(edge[1])
        else:
            return False
        self.graph[hor][ver] = '0'
        self.graph[ver][hor] = '0'
        return True
    def getNeighbors(self,vertex):
        if vertex not in self.vertices:
            return False
        inds = []
        neighbors = []
        count = 0
        for line in self.graph:
            if line[0] == vertex:
                for item in line:
                    if item == '1':
                        inds.append(count)
                    count+=1
        for ind in inds:
            neighbors.append(self.vertices[ind-1])
        return neighbors
    def printGraph(self):
        for line in self.graph:
            print(line)
    from collections import deque


class AdjacencyList:
    def __init__(self):
        self.adjList = {}
    def readGraph(self,filepath):
        fi = open(filepath)
        val = fi.readline().split()
        edgeCount = int(val[1])
        vertices = fi.readline().strip().split(',')
        for vertex in vertices:
            self.adjList.update({vertex:[]})
        for _ in range(edgeCount):
            edge = fi.readline().strip().split(' ')
            for key,value in self.adjList.items():
                if key == edge[0]:
                    value.append(edge[1])
                if key == edge[1]:
                    value.append(edge[0])
        return True
    def addVertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList.update({vertex:[]})
            return True
        else:
            return False
    def addEdge(self,edge):
        for key,value in self.adjList.items():
            if key == edge[0]:
                value.append(edge[1])
            if key == edge[1]:
                value.append(edge[0])
        return True
    def deleteVertex(self,vertex):
        if vertex in self.adjList:
            self.adjList.pop(vertex)
            return True
        else:
            return False
    def deleteEdge(self,edge):
        for key,value in self.adjList.items():
            if key == edge[0]:
                value.remove(edge[1])
            if key == edge[1]:
                value.remove(edge[0])
        return True
    def getNeighbors(self,vertex):
        return self.adjList.get(vertex)
    def printList(self):
        for key,value in self.adjList.items():
            print(key,value)
def BFS(graph, start_vertex, end_vertex):
    if start_vertex not in graph.adjList.keys() or end_vertex not in graph.adjList.keys():
        return False

    visited = set()
    queue = deque([(start_vertex, [])])

    while queue:
        vertex, path = queue.popleft()
        if vertex == end_vertex:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.adjList[vertex]:
                queue.append((neighbor, path + [(vertex, neighbor)]))
    return []

def DFS(graph, start_vertex, end_vertex):
    if start_vertex not in graph.adjList.keys() or end_vertex not in graph.adjList.keys():
        return False

    visited = set()
    stack = [(start_vertex, [])]

    while stack:
        vertex, path = stack.pop()
        if vertex == end_vertex:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.adjList[vertex]:
                stack.append((neighbor, path + [(vertex, neighbor)]))
    return []
fpath = input("File Path: ")

newMat = AdjacencyMatrix()
print("reading:",newMat.readGraph(fpath))
print("Adding 'u':",newMat.addVertex('u'))
print("adding edge to a,b:",newMat.addEdge(('a','b')))
print("adding edge to a,z:",newMat.addEdge(('a','z')))
newMat.printGraph()
print("deleting edge at a,b:",newMat.deleteEdge(('a','b')))
print("deleting vertex 'u':",newMat.deleteVertex('u'))
newMat.printGraph()
print("getting neighbors of 't':",newMat.getNeighbors('t'))

newList = AdjacencyList()
print("reading:",newList.readGraph(fpath))
print("add vertex 'u':",newList.addVertex('u'))
print("add edge 'd,h':",newList.addEdge(('d','h')))
newList.printList()
print("remove vertex 'u':",newList.deleteVertex('u'))
print("removing edge 'd,h':",newList.deleteEdge(('d','h')))
newList.printList()
print("neighbors of 'd':",newList.getNeighbors('d'))
print("")
print("bfs and dfs")
print("BFS from 'a' to 'p':", BFS(newList,'a', 'p'))
print("DFS from 'a' to 'p':", DFS(newList, 'a', 'p'))
print("BFS from 'n' to 'b':", BFS(newList, 'n', 'b'))
print("DFS from 'n' to 'b':", DFS(newList, 'n', 'b'))
print("BFS from 'g' to 'q':", BFS(newList, 'g', 'q'))
print("DFS from 'g' to 'q':", DFS(newList, 'g', 'q'))
print("BFS from 'c' to 'o':", BFS(newList, 'c', 'o'))
print("DFS from 'c' to 'o':", DFS(newList, 'c', 'o'))
print("BFS from 'o' to 'p':", BFS(newList, 'o', 'p'))
print("DFS from 'o' to 'p':", DFS(newList, 'o', 'p'))