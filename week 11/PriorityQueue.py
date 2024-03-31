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

    def insert(self, item, priority): #O(1) as it appends to the end, then sorts
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