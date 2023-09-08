class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, value):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > value:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(value)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.getNext()

        return count

    def search(self, value):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == value:
                found = True
            else:
                if current.getData() > value:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self, value):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == value:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous != None:
            previous.setNext(current.getNext())
            current.setNext(None)
        else:
            self.head = current.getNext()
            current.setNext(None)