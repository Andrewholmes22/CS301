class Node:
    def __init__(self, root = -1):
        self.item = root
        self.LeftChild = -1
        self.RightChild = -1

class AVLTree:
    def __init__(self,root,balance = 0):
        self.root = Node(root)
        self.balance = balance
        
    def balanced(self,curr_node = None):
        balance = []
        children = 0
        if curr_node is None:
            curr_node = self.root
        if curr_node.LeftChild>0:
            children-=1
        if curr_node.RightChild>0:
            children+=1
        balance.append([curr_node, children])
        self.balance = children
        while curr_node.LeftChild>-1:
            self.balanced(curr_node.LeftChild)
        while curr_node.RightChild>-1:
            self.balanced(curr_node.RightChild)
        print(balance)
        
    
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
    #worst case is O(n), where 'n' is the number of nodes in the tree
    
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
    #best case is O(1), when the item being searched for is found at the root 
    #worst case is O(n), when the item being searched is not in the tree or is at the last level of the tree
    
    def sorted_list(self, start=None):
        sortList = []
        if start is None:
            start = self.root
        if start.LeftChild != -1:
            sortList += self.sorted_list(start.LeftChild)
        sortList.append(start.item)
        if start.RightChild != -1:
            sortList += self.sorted_list(start.RightChild)
        return sortList
    #best case is O(n), when the tree is balanced, the algorithm would traverse each node once, adding each item to the sorted list.
    #worst case is O(n), when the tree is unbalanced each node only having one child needs to traverse all 'n' nodes in the tree recursively
    
    def reverse_sorted_list(self,start = None):
        if start == None:
            start = self.root
        sortList = []
        if start.RightChild != -1:
            self.reverse_sorted_list(start = start.RightChild)
        elif start.RightChild == -1:
            sortList.append(start.item)
        return sortList
    # best case O(n) when the tree is perfectly balanced, and every node has both a left and right child
    # worst case is O(n), when the tree is unbalanced each node only having one child needs to traverse all 'n' nodes in the tree recursively         
biTree = AVLTree(5)
biTree.insert(4)
biTree.insert(6)
biTree.insert(3)
biTree.insert(7)
print(biTree.search(5))#return True
print(biTree.search(9))#return False
print(biTree.search(7))#return True
print(biTree.search(3))#return True
print(biTree.sorted_list())
biTree.balanced()
