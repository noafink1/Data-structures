class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(2)
    q.enqueue(6)
    print(q.dequeue())

    
