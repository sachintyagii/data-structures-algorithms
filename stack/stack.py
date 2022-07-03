class MyStack:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def push(self, data):
        if self.size() == self.capacity:
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

def main():
    stack = MyStack(10)

    while(True):
        print('-----Select below option to perform operation:-----')
        print('1 - Push Operation')
        print('2 - Pop Operation')
        print('3 - Peek Operation')
        print('4 - Print Stack')
        print('5 - Exit')
        selected_option = int(input('Enter: '))

        match selected_option:
            case 1:
                data = input('Enter data : ')
                try:
                    stack.push(data)
                except Exception as e:
                    print(e)
            case 2:
                try:
                    stack.pop()
                except Exception as e:
                    print(e)
            case 3:
                try:
                    peek_data = stack.peek()
                    print(f'Peek data: {peek_data}')
                except Exception as e:
                    print(e)
            case 4:
                print( '->'.join(stack.stack[::-1]) )
            case 5:
                print('Thank You!')
                exit()
            case default:
                print('Not a valid option.')

if __name__ == '__main__':
    main()
