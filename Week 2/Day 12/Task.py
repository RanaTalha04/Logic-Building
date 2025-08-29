# Implement stack (push/pop).

class stack:

    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack is overflowed! ")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack is underflowed! ")
            return None
        else:
            value = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return value
    
    def display(self):
        if self.top == -1:
            print("Stack is empty ! ")
        else:
            print("Stack elements:", self.stack[:self.top+1])


size = int(input("Enter the size of stack: "))
s = stack(size)
i = 0
while i < size:
    element = int(input("Enter an element to push to stack: "))
    s.push(element)
    i += 1
s.display()

print("Popped:", s.pop())
s.display()