class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self):
        if len(self.queue) == self.capacity:
            return True
        return False

    def dequeue(self):
        if len(self.queue) == 0:
            raise "Queue is empty"
        else:
            firstElement =  self.queue[0]
            del firstElement


    def enqueue(self, value):
        if len(self.queue) == self.capacity:
            raise "Queue is full"
        else:
            self.queue.append(value)

    def front(self):
        return self.queue[0]

    def showQueue(self):
        return self.queue

if __name__ == "__main__":
    capacity = int(input())
    queue1 = Queue(capacity)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.isFull())
    print(queue1.showQueue())
