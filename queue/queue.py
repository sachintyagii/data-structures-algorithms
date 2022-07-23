class MyQueue:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return self.front==-1 and self.rear==-1

    def is_full(self):
        return len(self.queue)==self.capacity

    def enqueue(self, data):
        if self.is_full():
            print('Queue is Full.')
            exit(1)
        else:
            if self.is_empty():
                self.front += 1

            self.rear += 1
            self.queue.append(data)

    def dequeue(self):
        data = None
        if self.is_empty():
            print('Empty Queue.')
            exit(2)
        else:
            data = self.queue.pop(0)
            self.front += 1

            if self.front > self.rear:
                self.front = -1
                self.rear = -1
        return data

    def peek(self):
        data = None
        if self.is_empty():
            print('Empty Queue.')
            exit(2)
        else:
            data = self.queue[0]

        return data

    def display(self):
        print('->'.join(self.queue))

if __name__ == '__main__':
    q = MyQueue(10)

    q.enqueue('100')
    q.enqueue('200')
    q.enqueue('300')
    q.enqueue('400')
    print(q.peek())

    q.display()

    q.dequeue()
    q.display()
    print(q.peek())
