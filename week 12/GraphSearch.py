class AdjacencyMatrix:
    def __init__(self):
        self.graph = []
        self.vertices = []
    def readGraph(self,filepath):
        fi = open(filepath)
        num_verts,num_edges = fi.readline()
        print(num_verts,num_edges)
        
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
newMat.readGraph(fpath)