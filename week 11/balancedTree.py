class Node:
    def __init__(self, root = -1):
        self.item = root
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self,root,balance = 0):
        self.root = Node(root)
        self.balance = balance
        
    def insert(self, root, key):
	
        if not root:
            return Node(key)
        elif key < root.item:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        b = self.getBalance(root)

        if b > 1 and key < root.left.item:
            return self.rightRotate(root)

        if b < -1 and key > root.right.item:
            return self.leftRotate(root)

        if b > 1 and key > root.left.item:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if b < -1 and key < root.right.item:
            root.right = self.rightRotate(root.reft)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        temp = y.left

        y.left = z
        z.right = temp

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        temp2 = y.right

        y.right = z
        z.left = temp2

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def getHeight(self, root):
            if not root:
                return 0

            return root.height

    def getBalance(self, root):
            if not root:
                return 0
            return self.getHeight(root.left) - self.getHeight(root.right)

    
    def search(self, item):
        curr_node = self.root
        while curr_node is not None:
            if item == curr_node.item:
                return True
            elif item < curr_node.item:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False
    
    def sorted_list(self, start=None):
        sortList = []
        if start is None:
            start = self.root

        if start.left is not None:
            sortList += self.sorted_list(start.left)
            
        sortList.append(start.item)
        
        if start.right is not None:
            sortList += self.sorted_list(start.right)

        return sortList
 
    def reverse_sorted_list(self, start=None):
        if start is None:
            start = self.root
        sortList = []
        if start.right is not None:
            sortList += self.reverse_sorted_list(start.right)
        sortList.append(start.item)
        if start.left is not None:
            sortList += self.reverse_sorted_list(start.left)
        return sortList
    
Tree = AVLTree(0)  
Tree.root = Tree.insert(Tree.root, 1)
Tree.root = Tree.insert(Tree.root, 5)
Tree.root = Tree.insert(Tree.root, 7)
Tree.root = Tree.insert(Tree.root, 3)
Tree.root = Tree.insert(Tree.root, 8)
Tree.root = Tree.insert(Tree.root, 10)

print(Tree.search(5))  # return True
print(Tree.search(9))  # return False
print(Tree.search(7))  # return False
print(Tree.search(3))  # return True
print(Tree.sorted_list())
print(Tree.reverse_sorted_list())
