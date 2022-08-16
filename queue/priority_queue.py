class Node:
    def __init__(self):
        self.value = None
        self.priority = None

class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.queue = []

    def enqueue(self, value, priority):
        node = Node()
        node.value = value
        node.priority = priority
        self.queue.append(node)
        self.size += 1
        return True

    def peek(self):
        max_priority = self.queue[0].priority
        max_priority_index = 0

        for index in range(self.size):
            if max_priority < self.queue[index].priority:
                max_priority = self.queue[index].priority
                max_priority_index = index

        return max_priority_index

    def dequeue(self):
        index = self.peek()
        
        for i in range(index, self.size-1):
            self.queue[i] = self.queue[i+1]

        self.size -= 1
    
    def display(self):
        for i in range(self.size):
            print(f'({self.queue[i].value},{self.queue[i].priority})', end='->')
        print()

if __name__=="__main__":
    priority_queue = PriorityQueue(10)

    priority_queue.enqueue(100,10)
    priority_queue.enqueue(200,15)
    priority_queue.enqueue(300,10)
    priority_queue.enqueue(400,12)

    priority_queue.display()
    
    priority_queue.dequeue()
    priority_queue.display()
    priority_queue.dequeue()
    priority_queue.display()
    priority_queue.dequeue()
    priority_queue.display()
