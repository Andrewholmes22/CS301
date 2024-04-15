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
        for line in self.graph:
            if line[0] == vertex:
                for item in line:
                    if item == '1':
                        inds.append(line.index(item))
        for ind in inds:
            neighbors.append(self.vertices[ind-1])
        return neighbors
    def printGraph(self):
        for line in self.graph:
            print(line)

class AdjacencyList:
    def __init__(self):
        pass
    def readGraph(self,filepath):
        pass
    def addVertex(self,vertex):
        pass
    def addEdge(self,edge):
        pass
    def deleteVertex(self,vertex):
        pass
    def deleteEdge(self,edge):
        pass
    def getNeighbors(self,vertex):
        pass

fpath = input("File Path: ")

newMat = AdjacencyMatrix()
print("reading",newMat.readGraph(fpath))
print("Adding 'u'",newMat.addVertex('u'))
print("adding edge to a,b",newMat.addEdge(('a','b')))
print("adding edge to a,z",newMat.addEdge(('a','z')))
print("deleting edge at a,b",newMat.deleteEdge(('a','b')))
print("deleting vertex 'u'",newMat.deleteVertex('u'))
print("getting neighbors of 'j'",newMat.getNeighbors('j'))
#newMat.printGraph()