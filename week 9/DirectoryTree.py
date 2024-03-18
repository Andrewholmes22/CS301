class Node:
    def __init__(self, item):
        self.item = item
        self.children = []

class DirectoryTree:
    def __init__(self, root='/'):
        self.root = Node(root)

    def insert_file(self, path):
        directories = path.split('/')[1:]
        current_node = self.root

        for directory in directories[:-1]:
            found = False
            for child in current_node.children:
                if child.item == directory:
                    current_node = child
                    found = True
                    break
            if not found:
                new_node = Node(directory)
                current_node.children.append(new_node)
                current_node = new_node

        file_node = Node(directories[-1])
        current_node.children.append(file_node)

    def delete_file(self, path):
        directories = path.split('/')[1:]
        current_node = self.root

        for directory in directories[:-1]:
            found = False
            for child in current_node.children:
                if child.item == directory:
                    current_node = child
                    found = True
                    break
            if not found:
                raise IndexError('File Not Found')

        file_name = directories[-1]
        found = False
        for child in current_node.children:
            if child.item == file_name:
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
            print('  ' * depth + node.item)
            for child in node.children:
                self._print_tree_recursive(child, depth + 1)

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)


newTree = DirectoryTree()
newTree.insert_file('/usr')
newTree.insert_file('/var/log/log1.log')
newTree.insert_file('/var/log/log2.log')
newTree.insert_file('/dev/null')
newTree.insert_file('/dev/code/include')
newTree.insert_file('/dev/code/include/lib')
newTree.insert_file('/usr/patch')
newTree.insert_file('/usr/patch/log/log2.log')
newTree.insert_file('/usr/patch/log/log3.log')
newTree.insert_file('/mnt/c/users/local/program_data/VSCode/data.py')
newTree.print_tree()
newTree.delete_file('/usr/patch/log/log2.log')
newTree.print_tree()
newTree.move_file('/mnt/c/users/local/program_data/VSCode/data.py', '/usr/patch/log/data.py')
newTree.print_tree()