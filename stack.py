class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        return value

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(2)
    s.push(6)
    print(s.peek())
    s.pop()
    print(s.peek())