class Node():
    def __init__(self,item):
        self.item = item
        self.next = [None]
class DirectoryTree():
    def __init__(self,root='/'):
        self.root = root
        self.tree = [root]
    def insertPath(self,path):
        pathLi = path.split('/')
        pathLi.pop(0)
        while len(pathLi)>1:
            if pathLi[0] not in self.tree:
                    self.tree.append(DirectoryTree(root=pathLi[0]))
                    pathLi.pop(0)
            else:
                self.tree.insert(pathLi.index(pathLi[0]),DirectoryTree(root=pathLi[1]))
                pathLi.pop(0)
                pathLi.pop(1)
            
    def printTree(self):
        print(self.tree)

newTree = DirectoryTree()
newTree.printTree()
newTree.insertPath('/usr/log/log1')
newTree.printTree()
newTree.insertPath('/usr/log/log2')
newTree.printTree()

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None

    def add(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            
        else:
            newNode.next = self.head
            self.head = newNode

    def remove(self, item):
        if self.head is None:
            raise KeyError
        elif self.head.item == item:
            self.head = self.head.next
            return
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.next is None:
                    raise KeyError
                elif currentNode.next.item == item:
                    currentNode.next = currentNode.next.next
                    return

                currentNode = currentNode.next

    def search(self, item):
        currentNode = self.head
        while currentNode:
            if currentNode.item == item:
                return True
            currentNode = currentNode.next
        return False
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def size(self):
        currentNode = self.head
        counter = 0
        if self.head is None:
            return 0
        else:
            while currentNode:
                counter += 1
                currentNode = currentNode.next
            return counter

    def printAll(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.item)
            currentNode = currentNode.next

    def append(self, item):
        newNode = Node(item)
        currentNode = self.head
        if self.head is None:
            self.add(item)
        else:
            while currentNode:
                if currentNode.next is None:
                    currentNode.next = newNode
                    return
                currentNode = currentNode.next

    def index(self, item):
        currentNode = self.head
        counter = 0
        if self.head is None:
            raise KeyError
        else:
            while currentNode:
                if currentNode.item == item:
                    return counter
                currentNode = currentNode.next
                counter += 1
            raise KeyError
        
    def insert(self, position, item):
        currentNode = self.head
        newNode = Node(item)
        counter = 1
        if self.size() <= position:
            raise ValueError
        elif position == 0:
            self.add(item)
        else:
            while currentNode:
                if counter == position:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    return
                currentNode = currentNode.next
                counter += 1

    def pop(self, pos = None):
        currentNode = self.head
        counter = 1
        if self.head is None:
            raise ValueError
        
        elif pos == None or pos == self.size()-1:
            while currentNode:
                if currentNode.next.next is None:
                    returnItem = currentNode.next
                    currentNode.next = None
                    return returnItem

                currentNode = currentNode.next

        elif self.size() <= pos:
            raise ValueError

        elif pos == 0:
            returnItem = self.head
            self.head = currentNode.next
            return returnItem

        else:
            while currentNode:
                if counter == pos:
                    returnItem = currentNode.next
                    currentNode.next = currentNode.next.next
                    return returnItem
                counter += 1
                currentNode = currentNode.next
