class MyStack:
    def __init__(self, capacity):
        self.top = -1
        self.max = capacity
        self.stack = []

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def push(self, data):
        if self.size() == self.max:
            raise Exception('Stack Overflow.')

        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack Underflow.')

        self.stack.pop()
        self.top -= 1

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        
        return self.stack[self.top]

stack = MyStack(10)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
stack.push(80)
stack.push(90)
stack.push(100)
stack.push(101)

print(stack.peek())
stack.pop()
print(stack.peek())

print(f'Top: {stack.top}')

for i in stack.stack[::-1]:
    print(i)
