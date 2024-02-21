class linkedlist:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        current = self
        while current.next != None:
            current = current.next
        current.next = linkedlist(data)

    def prepend(self, data):
        new_node = linkedlist(data)
        new_node.next = self
        self = new_node
        return self

    def insert(self, data, index):
        current = self
        if index == 0:
            self = self.prepend(data)
            return self
        for i in range(index - 1):
            current = current.next
        new_node = linkedlist(data)
        new_node.next = current.next
        current.next = new_node
        return self

    def delete(self, index):
        current = self
        if index == 0:
            self = self.next
            return self
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next
        return self

    def print(self):
        current = self
        while current != None:
            print(current.data)
            current = current.next

    def reverse(self):
        current = self
        previous = None
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self = previous
        return self

    def search(self, data):
        current = self
        index = 0
        while current != None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def sort(self):
        current = self
        while current != None:
            next = current.next
            while next != None:
                if current.data > next.data:
                    temp = current.data
                    current.data = next.data
                    next.data = temp
                next = next.next
            current = current.next
        return self

    def length(self):
        current = self
        length = 0
        while current != None:
            length += 1
            current = current.next
        return length

    def get(self, index):
        current = self
        for i in range(index):
            current = current.next
        return current.data

    def set(self, data, index):