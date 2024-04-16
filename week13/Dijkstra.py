class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item, priority): #O(1) as it appends to the end, then sorts. Sorting is 0(log n)
        self.heap.append((item, priority))
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i): #O(log n), sorting is done quickly by heap rules, not fully sorted rules
        while i > 0 and self.heap[i][1] > self.heap[self.parent(i)][1]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i): #O(log n), same as heaping up, this is quite quick
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left][1] > self.heap[max_index][1]:
            max_index = left

        if right < len(self.heap) and self.heap[right][1] > self.heap[max_index][1]:
            max_index = right

        if i != max_index:
            self.swap(i, max_index)
            self.heapify_down(max_index)

    def pop(self): #pop is fast, calling from the end means it doesn't need to shift anything. O(log n) from sorting
        if len(self.heap) == 0:
            return None

        max_element = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self.heapify_down(0)
        return max_element
    
    def returnQueue(self):
        outQueue = self.heap
        return outQueue

class AdjacencyList:
    def __init__(self):
        self.adjList = {}
        self.vertices = []
    def readGraph(self,filepath):
        fi = open(filepath)
        val = fi.readline().split()
        edgeCount = int(val[1])
        vertices = fi.readline().strip().split(',')
        for vertex in vertices:
            self.vertices.append(vertex)
            self.adjList.update({vertex:[]})
        for _ in range(edgeCount):
            edge = fi.readline().strip().split(' ')
            for key,value in self.adjList.items():
                if key == edge[0]:
                    value.append((edge[1],edge[2]))
                if key == edge[1]:
                    value.append((edge[0],edge[2]))
        fi.close()
        return True
    def addVertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList.update({vertex:[]})
            return True
        else:
            return False
    def addEdge(self,edge):
        if edge[0] in self.vertices and edge[1] in self.vertices:
            for key,value in self.adjList.items():
                if key == edge[0]:
                    value.append((edge[1],edge[2]))
                if key == edge[1]:
                    value.append((edge[0],edge[2]))
            return True
        else:
            return False
    def deleteVertex(self,vertex):
        for key,value in self.adjList.items():
            for tup in value:
                if vertex in tup:
                    value.remove(tup)
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
            
def Dijkstra(graph,start,end):
    pass

fpath1 = '/home/cye/AlgosHW/REPO2/CS301/week13/weightedGraph1.txt'
fpath2 = '/home/cye/AlgosHW/REPO2/CS301/week13/weightedGraph2.txt'


wGraph1 = AdjacencyList()
wGraph1.readGraph(fpath1)
wGraph2 = AdjacencyList()
wGraph2.readGraph(fpath2)
print("Graph 1 start:")
wGraph1.printList()
print("Graph 2 start:")
wGraph2.printList()
wGraph1.deleteVertex('j')
wGraph2.deleteVertex('i')
print("Graph 1 deleted vert j:")
wGraph1.printList()
print("Graph 2 deleted vert i:")
wGraph2.printList()
wGraph1.addVertex('j')
wGraph2.addVertex('i')
wGraph1.addEdge(('j','a','10'))
wGraph1.addEdge(('j','b','4'))
wGraph2.addEdge(('i','c','1'))
print("Graph 1 added vert j and edges:")
wGraph1.printList()
print("Graph 2 added vert i and edge:")
wGraph2.printList()