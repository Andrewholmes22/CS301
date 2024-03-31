class PriorityQueue:
    def __init__(self):
        self.queue = []
    def sortFunc(self,tup):
        tup = tup
        return tup[1]
    def sortQueue(self): 
        self.queue.sort(reverse = True,key=self.sortFunc)
        #python sort is very efficient, O(n log n)
    def insert(self,item,priority): 
        tempTuple = (item,priority)
        self.queue.append(tempTuple)
        self.sortQueue()
        #this is very fast, O(1), as it inserts the item at the end
    def pop(self): 
        out = self.queue.pop(0)
        self.sortQueue()
        return out
        #this is probably the slowest, O(n), as it pops from the front
        #but depending on need it could swap speeds with insert
    def returnQueue(self):
        outQueue = self.queue
        return outQueue
        #O(n) as it copies and sends out a different list.

newPriQueue = PriorityQueue()
newPriQueue.insert(1,4)
newPriQueue.insert(2,3)
newPriQueue.insert(3,2)
newPriQueue.insert(4,1)
newPriQueue.insert(5,1)
print(newPriQueue.returnQueue())
print(newPriQueue.pop())
print(newPriQueue.returnQueue())
        
        