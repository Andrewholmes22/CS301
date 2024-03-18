class Node():
    def __init__(self,item):
        self.item = item
        self.next = [None]
class DirectoryTree():
    def __init__(self,root='/'):
        self.root = root
        self.tree = [root]
    def insert_file(self,path):
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
            
    def delete_file(self, path):
        directories = path.split('/')[1:]
        current_node = self.root

        for directory in directories[:-1]:
            found = False
            for child in current_node.children:
                if child.data == directory:
                    current_node = child
                    found = True
                    break
            if not found:
                raise IndexError('File Not Found')

        file_name = directories[-1]
        found = False
        for child in current_node.children:
            if child.data == file_name:
                current_node.children.remove(child)
                found = True
                break

        if not found:
            raise IndexError('File Not Found')

    def move_file(self, source_path, destination_path):
        try:
            self.insert_file(destination_path)
            self.delete_file(source_path)
        except IndexError as e:
            raise IndexError(str(e))

    def _print_tree_recursive(self, node, depth):
        if isinstance(node, Node):
            print('  ' * depth + node.data)
            for child in node.children:
                self._print_tree_recursive(child, depth + 1)
        else:
            print('  ' * depth + node)

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)


newTree = DirectoryTree()
newTree.insert_file('/usr/log/log1')
newTree.insert_file('/usr/log/log2')
newTree.print_tree()
