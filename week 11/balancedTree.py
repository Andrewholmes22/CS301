class Node:
    def __init__(self, root = -1):
        self.item = root
        self.left = -1
        self.right = -1

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

        root.height = 1 + max(self.getHeight(root.left),
                        self.getHeight(root.right))

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
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

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
biTree = AVLTree(5)  # Initialize AVL tree with root value 5
root = biTree.root
biTree.insert(root, 4)  # Pass the root node to the insert function
biTree.insert(root, 6)
biTree.insert(root, 3)
biTree.insert(root, 7)
print(biTree.search(5))#return True
print(biTree.search(9))#return False
print(biTree.search(7))#return True
print(biTree.search(3))#return True
print(biTree.sorted_list())
