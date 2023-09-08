class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, value):
        self.items.insert(0, value)

    def addRear(self, value):
        self.items.append(value)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    d = Deque()
    d.addRear(1)
    d.addRear(2)
    d.addRear(3)
    print(d.removeFront())
    print(d.removeRear())