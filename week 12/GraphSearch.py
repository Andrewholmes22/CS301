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
        for line in self.graph:
            print(line)
        return True
    def addVertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.graph.append(vertex)
            for line in self.graph:
                if line == 1:
                    self.graph.append(vertex)
                else:
                    self.graph.append('0')
        return True
    def addEdge(self,edge):
        pass
    def deleteVertex(self,vertex):
        pass
    def deleteEdge(self,edge):
        pass
    def getNeighbors(self,vertex):
        pass

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
print(newMat.readGraph(fpath))
#print(newMat.addVertex('u'))