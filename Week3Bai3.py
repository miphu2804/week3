class Stack:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def is_full(self):
        if len(self.stack) == capacity:
            return True
        return False

    def top(self):
        if len(self.stack) == 0:
            raise "Stack is empty"
        else:
            return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            raise "Stack is empty"
        else:
            return self.stack.pop(-1)

    def push(self, value):
        if len(self.stack) == capacity:
            raise "Stack is full"
        else:
            return self.stack.append(value)

    def showStack(self):
        print(self.stack)
if __name__ == "__main__":
    capacity = int(input())
    stack1 = Stack(capacity)
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.showStack()
    print(stack1.is_full())
