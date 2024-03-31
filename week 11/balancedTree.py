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

pq = PriorityQueue()
pq.insert("task1", 5)
pq.insert("task2", 3)
pq.insert("task3", 8)
pq.insert("task4", 2)
print(pq.returnQueue())
pq.pop()
pq.pop()
print(pq.returnQueue())
    
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
