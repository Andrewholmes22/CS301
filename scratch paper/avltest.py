class Node:
    def __init__(self, root = -1):
        self.item = root
        self.LeftChild = -1
        self.RightChild = -1
class avltree:
    def __init__(self,root):
        self.root = Node(root)
        self.balance = 0
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
    def balance(self,curr_node = None):
        balance = []
        children = 0
        if curr_node == None:
            curr_node = self.root
        if curr_node.LeftChild>0:
            children-=1
        if curr_node.RightChild>0:
            children+=1
        balance.append([curr_node, children])
        while curr_node.LeftChild>-1:
            balance(curr_node.LeftChild)
        while curr_node.RightChild>-1:
            balance(curr_node.RightChild)
        print(balance)
        
    def rotateRight(self,curr_node):
        if curr_node.LeftChild == -1:
            return
        else:
            temp = curr_node.LeftChild
            curr_node.LeftChild = temp.RightChild
            temp.RightChild = curr_node
            return temp
    def rotateLeft(self,curr_node):
        if curr_node.RightChild == -1:
            return
        else:
            temp = curr_node.RightChild
            curr_node.RightChild = temp.LeftChild
            temp.LeftChild = curr_node
            return temp
    def rotateRightLeft(self,curr_node):
        curr_node.RightChild = self.rotateRight(curr_node.Right