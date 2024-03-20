class Node:
    def __init__(self, item):
        self.item = item
        self.children = []

class DirectoryTree:
    def __init__(self, root='/'):
        self.root = Node(root)