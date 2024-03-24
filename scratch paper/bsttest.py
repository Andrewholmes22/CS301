class Node:
    def __init__(self, root=-1):
        self.item = root
        self.LeftChild = -1
        self.RightChild = -1

class DirectoryTree:
    def __init__(self, root):
        self.root = Node(root)
        
    def insert(self, item):
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
                    
    def search(self, item):
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
    
    def reverse_sorted_list(self, start=None):
        sortList = []
        if start is None:
            start = self.root
        if start.RightChild != -1:
            sortList += self.reverse_sorted_list(start.RightChild)
        sortList.append(start.item)
        if start.LeftChild != -1:
            sortList += self.reverse_sorted_list(start.LeftChild)
        return sortList

# Example usage:
biTree = DirectoryTree(5)
biTree.insert(4)
biTree.insert(6)
biTree.insert(3)
biTree.insert(7)
print(biTree.search(5))  # Output: True
print(biTree.search(9))  # Output: False
print(biTree.search(7))  # Output: True
print(biTree.search(3))  # Output: True
print(biTree.sorted_list())  # Output: [3, 4, 5, 6, 7]
print(biTree.reverse_sorted_list())