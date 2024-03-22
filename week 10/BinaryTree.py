class Node:
    def __init__(self, root = -1):
        self.item = root
        self.LeftChild = -1
        self.RightChild = -1

class DirectoryTree:
    def __init__(self,root):
        self.root = Node(root)
        
    def insert(self,item):
        current_node = self.root
        Found = False
        while not Found:
            if item <= current_node.item:
                if current_node.LeftChild == -1:
                    current_node.LeftChild = Node(item)
                    Found = True
                    break
                else:
                    current_node = current_node.LeftChild
            elif item > current_node.item:
                if current_node.RightChild == -1:
                    current_node.RightChild = Node(item)
                    Found = True
                    break
                else:
                    current_node = current_node.RightChild
    def search(self,item):
        curr_node = self.root
        found = False
        while not found:
            if item == curr_node.item:
                found = True
                return True
            elif curr_node.LeftChild == -1 and curr_node.RightChild == -1:
                return False
            elif item <= curr_node.item:
                curr_node = curr_node.LeftChild
            elif item > curr_node.item:
                curr_node = curr_node.RightChild
    def sorted_list(self,start = None):
        if start == None:
            start = self.root
        sortList = []
        if start.LeftChild != -1:
            self.sorted_list(start = start.LeftChild)
        elif start.LeftChild == -1:
            sortList.append(start.item)
        
                
biTree = DirectoryTree(5)
biTree.insert(4)
biTree.insert(6)
biTree.insert(3)
biTree.insert(7)
print(biTree.search(5))
print(biTree.search(9))
print(biTree.search(7))
print(biTree.search(3))
print(biTree.sorted_list())
