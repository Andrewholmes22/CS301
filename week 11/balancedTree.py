class Node:
    def __init__(self, root = -1):
        self.item =root
        self.left = -1
        self.right = -1
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

    
    def search(self,item):
        curr_node = self.root
        found = False
        while not found:
            if item == curr_node.item:
                found = True
                return True
            elif curr_node.left == -1 and curr_node.right == -1:
                return False
            elif item <= curr_node.item:
                curr_node = curr_node.Left
            elif item > curr_node.item:
                curr_node = curr_node.Right
    #best case is O(1), when the item being searched for is found at the root 
    #worst case is O(n), when the item being searched is not in the tree or is at the last level of the tree
    
    def sorted_list(self, start=None):
        sortList = []
        if start is None:
            start = self.root
        if start.left != -1:
            sortList += self.sorted_list(start.lefteft)
        sortList.append(start.item)
        if start.right != -1:
            sortList += self.sorted_list(start.right)
        return sortList
    #best case is O(n), when the tree is balanced, the algorithm would traverse each node once, adding each item to the sorted list.
    #worst case is O(n), when the tree is unbalanced each node only having one child needs to traverse all 'n' nodes in the tree recursively
    
    def reverse_sorted_list(self,start = None):
        if start == None:
            start = self.root
        sortList = []
        if start.right != -1:
            self.reverse_sorted_list(start = start.right)
        elif start.right == -1:
            sortList.append(start.item)
        return sortList
    # best case O(n) when the tree is perfectly balanced, and every node has both a left and right child
    # worst case is O(n), when the tree is unbalanced each node only having one child needs to traverse all 'n' nodes in the tree recursively         
Tree = AVLTree(0)
root = None

Tree.insert(root, 1)
Tree.insert(root, 2)
Tree.insert(root, 3)
Tree.insert(root, 4)
Tree.insert(root, 5)
Tree.insert(root, 6)

print(Tree.search(5))#return True
print(Tree.search(9))#return False
print(Tree.search(7))#return True
print(Tree.search(3))#return True
print(Tree.sorted_list())
