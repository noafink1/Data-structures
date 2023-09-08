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

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, value):
        temp = Node(value)
        temp.setNext(self.head)
        self.head = temp

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
        while current != None and not found:
            if current.getData() == value:
                found = True
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

if __name__ == "__main__":
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))