# Implement queue (enqueue/dequeue)

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0  

    def enqueue(self, value):
        if self.count == self.size:
            print("Queue is full (Overflow).")
        else:
            self.rear += 1
            self.queue[self.rear] = value
            self.count += 1
            print("Enqueued.")

    def dequeue(self):
        if self.count == 0:
            print("Queue is empty (Underflow).")
        else:
            value = self.queue[self.front]
            
            for i in range(self.rear):
                self.queue[i] = self.queue[i+1]
            self.queue[self.rear] = None
            self.rear -= 1
            self.count -= 1
            print("Dequeued.")
            return value

    def display(self):
        if self.count == 0:
            print("Queue is empty.")
        else:
            print("Queue:", end=" ")
            for i in range(self.count):
                print(self.queue[i], end=" ")
            print()

    
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()
